from typing import List

from models.hotel import Hotel
from services.embedding_service import EmbeddingService
from services.metadata_service import MetadataService
from services.vector_search_service import VectorSearchService


class RecommendationEngine:

    MINIMUM_SIMILARITY = 0.30
    SEARCH_CANDIDATE_COUNT = 5000

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_search_service: VectorSearchService,
        metadata_service: MetadataService,
    ):
        self.embedding_service = embedding_service
        self.vector_search_service = vector_search_service
        self.metadata_service = metadata_service

    def recommend(
        self,
        query: str,
        destination: str,
        recommendation_count: int = 5,
        minimum_rating: float = 1.0,
        hotel_classes: List[str] = None,
    ) -> List[Hotel]:

        query_vector = self.embedding_service.encode(query)

        distances, indices = self.vector_search_service.search(
            query_vector=query_vector,
            top_k=self.SEARCH_CANDIDATE_COUNT,
        )

        selected_classes = {
            float(hotel_class.split()[0])
            for hotel_class in (hotel_classes or [])
        }

        normalized_destination = (
            destination.strip().casefold()
        )

        # Her otelden yalnızca en iyi eşleşen yorumu tutacağız.
        hotels_by_id = {}

        for distance, index in zip(distances, indices):

            if index < 0:
                continue

            metadata = self.metadata_service.get(
                int(index)
            )

            city = str(
                metadata.get("city", "")
            ).strip()

            if not self._destination_matches(
                city,
                normalized_destination,
            ):
                continue

            overall_rating = float(
                metadata.get("overall_rating", 0.0)
            )

            if overall_rating < minimum_rating:
                continue

            hotel_class = float(
                metadata.get("hotel_class", 0.0)
            )

            if (
                selected_classes
                and hotel_class not in selected_classes
            ):
                continue

            similarity = self._l2_to_cosine(
                distance
            )

            if similarity < self.MINIMUM_SIMILARITY:
                continue

            hotel = self._create_hotel(
                metadata,
                similarity,
            )

            current_hotel = hotels_by_id.get(
                hotel.offering_id
            )

            if (
                current_hotel is None
                or hotel.match > current_hotel.match
            ):
                hotels_by_id[
                    hotel.offering_id
                ] = hotel

        results = list(
            hotels_by_id.values()
        )

        results.sort(
            key=lambda hotel: (
                hotel.match,
                hotel.overall_rating,
            ),
            reverse=True,
        )

        return results[:recommendation_count]

    @staticmethod
    def _destination_matches(
        city: str,
        normalized_destination: str,
    ) -> bool:

        normalized_city = city.casefold()

        if (
            not normalized_city
            or not normalized_destination
        ):
            return False

        return (
            normalized_city
            == normalized_destination
            or normalized_destination
            in normalized_city
            or normalized_city
            in normalized_destination
        )

    @staticmethod
    def _l2_to_cosine(
        distance: float
    ) -> float:

        # Normalize edilmiş vektörlerde:
        # cosine_similarity = 1 - L2_distance / 2
        similarity = 1.0 - (
            float(distance) / 2.0
        )

        return max(
            0.0,
            min(1.0, similarity),
        )

    @staticmethod
    def _create_hotel(
        metadata,
        similarity: float,
    ) -> Hotel:

        return Hotel(
            offering_id=int(
                metadata["offering_id"]
            ),
            name=str(metadata["name"]),
            city=str(metadata["city"]),
            overall_rating=float(
                metadata["overall_rating"]
            ),
            hotel_class=float(
                metadata["hotel_class"]
            ),
            title=str(
                metadata.get("title", "")
            ),
            text=str(
                metadata.get("text", "")
            ),
            match=similarity,
            reason=(
                "Arama metninizle anlamsal olarak "
                "benzer bir misafir yorumu bulundu."
            ),
        )