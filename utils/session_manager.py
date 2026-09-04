import streamlit as st


class SessionManager:

    def initialize(self):

        defaults = {
            "recommendations": [],
            "searched_destination": "",
            "searched_query": "",
        }

        for key, value in defaults.items():

            if key not in st.session_state:
                st.session_state[key] = value

    def save_search(
        self,
        recommendations,
        destination,
        query,
    ):

        st.session_state["recommendations"] = recommendations
        st.session_state["searched_destination"] = destination
        st.session_state["searched_query"] = query

    def clear_recommendations(self):

        st.session_state["recommendations"] = []

    def get_recommendations(self):

        return st.session_state["recommendations"]

    def get_destination(self):

        return st.session_state["searched_destination"]