from dataclasses import dataclass


@dataclass
class Hotel:
    name: str
    hotel_class: int
    rating: float
    match: int
    reason: str
    review: str