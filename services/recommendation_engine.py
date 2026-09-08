from typing import List

from models.hotel import Hotel
from services.embedding_service import (
    EmbeddingService,
)
from services.vector_search_service import (
    VectorSearchService,
)
from services.metadata_service import (
    MetadataService,
)


class RecommendationEngine:

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_search_service: VectorSearchService,
        metadata_service: MetadataService,
    ):

        self.embedding_service = (
            embedding_service
        )

        self.vector_search_service = (
            vector_search_service
        )

        self.metadata_service = (
            metadata_service
        )

    def recommend(
        self,
        query: str,
        recommendation_count: int = 5,
        minimum_rating: float = 1.0,
        hotel_classes: List[str] = None,
    ) -> List[Hotel]:

        # ----------------------------------------
        # 1. User prompt → embedding
        # ----------------------------------------

        query_vector = (
            self.embedding_service.encode(
                query
            )
        )

        # ----------------------------------------
        # 2. Search FAISS
        # ----------------------------------------

        scores, indices = (
            self.vector_search_service.search(
                query_vector=query_vector,
                top_k=50,
            )
        )

        # ----------------------------------------
        # 3. Get metadata
        # ----------------------------------------

        results = []

        for score, index in zip(
            scores,
            indices,
        ):

            if index < 0:
                continue

            metadata = (
                self.metadata_service.get(
                    int(index)
                )
            )

            results.append(
                self._create_hotel(
                    metadata,
                    score,
                )
            )

        # ----------------------------------------
        # 4. Apply rating filter
        # ----------------------------------------

        results = [
            hotel
            for hotel in results
            if hotel.overall_rating >= minimum_rating
        ]

        # ----------------------------------------
        # 5. Apply hotel class filter
        # ----------------------------------------

        #if hotel_classes:

         #   selected_classes = {
          #      int(
           #         hotel_class.split()[0]
            #    )
             #   for hotel_class
              #  in hotel_classes
            #}

            #results = [
            #    hotel
            #    for hotel in results
            #    if hotel.hotel_class
            #    in selected_classes
            #]

        # ----------------------------------------
        # 6. Sort by semantic similarity
        # ----------------------------------------

        results.sort(
            key=lambda hotel: hotel.match,
            reverse=True,
        )

        return results[
            :recommendation_count
        ]

    @staticmethod
    def _create_hotel(
        metadata,
        score,
    ) -> Hotel:

        return Hotel(
            offering_id=int(metadata["offering_id"]),

            name=str(metadata["name"]),

            overall_rating=float(
                metadata["overall_rating"]
            ),

            title=str(
                metadata.get("title", "")
            ),

            match=float(score),

            reason=(
                "Bu otel, arama kriterinizle "
                "semantik olarak benzer olduğu için önerildi."
            ),
        )