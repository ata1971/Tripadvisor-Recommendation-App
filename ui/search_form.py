import streamlit as st


class SearchForm:

    def render(self):

        st.markdown(
            """
            <div class="brand-title">
                🏨 TripAdvisor <span>Hotel Finder</span>
            </div>

            <div class="brand-description">
                Gerçek misafir yorumlarına göre size uygun
                otelleri keşfedin.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="search-title">
                Mükemmel konaklama deneyimini bulun
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write(
            "Nasıl bir otel aradığınızı kendi kelimelerinizle anlatın."
        )

        with st.form("hotel_search_form"):

            query = st.text_area(
                "Otel tercihiniz",
                placeholder=(
                    "Örn: Merkezi konumda, sessiz, temiz ve "
                    "çocuklu ailelere uygun bir otel arıyorum."
                ),
                height=130,
                label_visibility="collapsed",
            )

            submit = st.form_submit_button(
                "🔍 Otelleri Bul"
            )

        return query, submit