import streamlit as st

from ui.hotel_card import HotelCard


class ResultsView:

    def render(
        self,
        recommendations,
        destination,
    ):

        if not recommendations:
            return

        st.divider()

        st.subheader(
            f"🏨 {destination} için önerilen oteller"
        )

        st.caption(
            "Sonuçlar şu anda prototip verilerle gösterilmektedir."
        )

        for index, hotel in enumerate(
            recommendations,
            start=1,
        ):

            HotelCard.render(
                hotel=hotel,
                index=index,
                destination=destination,
            )