import streamlit as st


class Sidebar:

    def render(self):

        with st.sidebar:

            st.header("🔎 Arama Filtreleri")

            destination = st.text_input(
                "Nereye gitmek istiyorsunuz?",
                placeholder="Örn: New York",
            )

            recommendation_count = st.slider(
                "Önerilecek otel sayısı",
                1,
                5,
                20,
            )

            minimum_rating = st.slider(
                "Minimum kullanıcı puanı",
                1.0,
                5.0,
                4.0,
                0.1,
            )

            hotel_classes = st.multiselect(
                "Otel sınıfı",
                [
                    "3 yıldız",
                    "4 yıldız",
                    "5 yıldız",
                ],
                default=[
                    "4 yıldız",
                    "5 yıldız",
                ],
            )

            travel_type = st.selectbox(
                "Seyahat türü",
                [
                    "Fark etmez",
                    "Aile tatili",
                    "Romantik tatil",
                    "İş seyahati",
                    "Tek başına seyahat",
                ],
            )

            st.divider()

            st.caption(
                "Bu ekran UI prototipidir. Gerçek öneri sistemi "
                "daha sonra bağlanacaktır."
            )

        return {
            "destination": destination,
            "recommendation_count": recommendation_count,
            "minimum_rating": minimum_rating,
            "hotel_classes": hotel_classes,
            "travel_type": travel_type,
        }