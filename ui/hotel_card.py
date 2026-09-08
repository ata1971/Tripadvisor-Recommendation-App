import streamlit as st

from models.hotel import Hotel


class HotelCard:

    @staticmethod
    def render(
        hotel: Hotel,
        index: int,
        destination: str,
    ):

        with st.container(border=True):

            name_column, rating_column = st.columns([4, 1])

            with name_column:

                st.subheader(
                    f"{index}. {hotel.name}"
                )

                st.write(
                    f"📍 {destination} · "
                    #f"{hotel.hotel_class} yıldızlı otel"
                )

            with rating_column:

                st.metric(
                    "Kullanıcı puanı",
                    f"{hotel.overall_rating:.1f}/5",
                )

            filled_circles = "●" * round(hotel.overall_rating)

            st.markdown(
                f"""
                <span style="
                    color:#00AA6C;
                    font-size:22px;
                    letter-spacing:3px;
                ">
                    {filled_circles}
                </span>
                """,
                unsafe_allow_html=True,
            )

            match_percentage = max(
                0.0,
                min(100.0, hotel.match * 100)
            )

            st.progress(
                match_percentage / 100,
                text=f"%{match_percentage:.1f} tercih uyumu",
            )

            st.write(
                f"**Neden önerildi?** {hotel.reason}"
            )

            with st.expander(
                "Eşleşen kullanıcı yorumunu göster"
            ):

                st.markdown(
                    f"> “{hotel.title}”"
                )