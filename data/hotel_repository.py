from typing import List

from models.hotel import Hotel


class HotelRepository:

    def __init__(self):
        self.hotels = self._load_hotels()

    def _load_hotels(self) -> List[Hotel]:
        return [
            Hotel(
                name="Central Park Boutique Hotel",
                hotel_class=5,
                rating=4.8,
                match=96,
                reason=(
                    "Merkezi konumu, sessiz odaları ve temizlik "
                    "hakkındaki olumlu yorumlarıyla eşleşiyor."
                ),
                review=(
                    "The rooms were spotless, quiet and within "
                    "walking distance of the city center."
                ),
            ),

            Hotel(
                name="Riverside Family Hotel",
                hotel_class=4,
                rating=4.6,
                match=92,
                reason=(
                    "Aile dostu hizmetleri, geniş odaları ve sakin "
                    "konumuyla tercihlerinize uyuyor."
                ),
                review=(
                    "A comfortable and peaceful hotel, especially "
                    "suitable for families with children."
                ),
            ),

            Hotel(
                name="City Garden Residence",
                hotel_class=4,
                rating=4.5,
                match=89,
                reason=(
                    "Ulaşım kolaylığı, temizliği ve güler yüzlü "
                    "personeliyle öne çıkıyor."
                ),
                review=(
                    "Very clean, friendly staff and easy access "
                    "to public transportation."
                ),
            ),

            Hotel(
                name="Grand Avenue Hotel",
                hotel_class=5,
                rating=4.4,
                match=86,
                reason=(
                    "Merkezi konumu ve yüksek hizmet kalitesi "
                    "nedeniyle öneriliyor."
                ),
                review=(
                    "Excellent location with professional service "
                    "and comfortable rooms."
                ),
            ),

            Hotel(
                name="Green Square Inn",
                hotel_class=3,
                rating=4.2,
                match=82,
                reason=(
                    "Uygun fiyatı, temiz odaları ve sakin çevresiyle "
                    "iyi bir alternatif oluşturuyor."
                ),
                review=(
                    "A clean and quiet place offering good value "
                    "for the price."
                ),
            ),
        ]

    def get_all_hotels(self) -> List[Hotel]:
        return self.hotels