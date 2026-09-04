import streamlit as st

from data.hotel_repository import HotelRepository
from services.recommendation_engine import RecommendationEngine
from utils.session_manager import SessionManager

from ui.styles import StyleManager
from ui.sidebar import Sidebar
from ui.search_form import SearchForm
from ui.results_view import ResultsView


class HotelRecommendationApp:

    def __init__(self):

        self.repository = HotelRepository()

        self.engine = RecommendationEngine(
            self.repository
        )

        self.session = SessionManager()

        self.sidebar = Sidebar()
        self.search_form = SearchForm()
        self.results_view = ResultsView()

    def configure_page(self):

        st.set_page_config(
            page_title="TripAdvisor Hotel Finder",
            page_icon="🏨",
            layout="wide",
            initial_sidebar_state="expanded",
        )

    def validate_input( 
        self,
        destination,
        query,
    ):

        if not destination.strip():

            st.warning(
                "Lütfen sol panelden gitmek istediğiniz "
                "yeri yazın."
            )

            self.session.clear_recommendations()

            return False

        if not query.strip():

            st.warning(
                "Lütfen nasıl bir otel aradığınızı açıklayın."
            )

            self.session.clear_recommendations()

            return False

        return True

    def handle_search(
        self,
        filters,
        query,
    ):

        recommendations = self.engine.recommend(
            query=query,
            destination=filters["destination"],
            recommendation_count=filters[
                "recommendation_count"
            ],
            minimum_rating=filters[
                "minimum_rating"
            ],
            hotel_classes=filters[
                "hotel_classes"
            ],
        )

        if not recommendations:

            st.info(
                "Seçtiğiniz filtrelere uygun örnek otel "
                "bulunamadı."
            )

        self.session.save_search(
            recommendations=recommendations,
            destination=filters["destination"],
            query=query,
        )

    def run(self):

        self.configure_page()

        StyleManager.apply()

        self.session.initialize()

        filters = self.sidebar.render()

        query, submit = self.search_form.render()

        if submit:

            if self.validate_input(
                filters["destination"],
                query,
            ):

                self.handle_search(
                    filters,
                    query,
                )

        recommendations = (
            self.session.get_recommendations()
        )

        destination = (
            self.session.get_destination()
        )

        self.results_view.render(
            recommendations,
            destination,
        )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    app = HotelRecommendationApp()

    app.run()