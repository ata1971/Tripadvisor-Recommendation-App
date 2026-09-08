from dataclasses import dataclass


@dataclass
class Hotel:

    #id: int
    name: str
    #city: str
    #state: str
    title: str
    offering_id: int
    #service_rating: float
    #cleanliness_rating: float
    overall_rating: float
    #value_rating: float
    #location_rating: float
    #sleep_quality_rating: float
    #rooms_rating: float

    match: float = 0.0
    reason: str = ""