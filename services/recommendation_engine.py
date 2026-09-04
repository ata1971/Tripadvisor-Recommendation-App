from typing import List

from models.hotel import Hotel
from data.hotel_repository import HotelRepository


class RecommendationEngine:

    def __init__(self, repository: HotelRepository):
        self.repository = repository

    def recommend(
        self,
        query: str,
        destination: str,
        recommendation_count: int,
        minimum_rating: float,
        hotel_classes: List[str],
    ) -> List[Hotel]:

        selected_classes = {
            int(hotel_class.split()[0])
            for hotel_class in hotel_classes
        }

        hotels = self.repository.get_all_hotels()

        filtered_hotels = [
            hotel
            for hotel in hotels
            if (
                hotel.rating >= minimum_rating
                and hotel.hotel_class in selected_classes
            )
        ]

        filtered_hotels.sort(
            key=lambda hotel: hotel.match,
            reverse=True,
        )

        return filtered_hotels[:recommendation_count]