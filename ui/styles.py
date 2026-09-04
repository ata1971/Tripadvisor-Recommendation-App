import streamlit as st


class StyleManager:

    @staticmethod
    def apply():

        st.markdown(
            """
            <style>

            .block-container {
                max-width: 1180px;
                padding-top: 2.5rem;
                padding-bottom: 3rem;
            }

            section[data-testid="stSidebar"] {
                border-right: 1px solid #e0e0e0;
            }

            .brand-title {
                font-size: 38px;
                font-weight: 800;
                color: #000000;
                margin-bottom: 4px;
            }

            .brand-title span {
                color: #00aa6c;
            }

            .brand-description {
                color: #545454;
                font-size: 17px;
                margin-bottom: 30px;
            }

            .search-title {
                font-size: 30px;
                font-weight: 750;
                color: #000000;
                margin-bottom: 5px;
            }

            div[data-testid="stForm"] {
                border: 1px solid #dedede;
                border-radius: 18px;
                padding: 24px;
                box-shadow:
                    0 4px 16px rgba(0, 0, 0, 0.07);
            }

            .stTextArea textarea {
                border-radius: 14px;
                border: 2px solid #d6d6d6;
            }

            .stTextArea textarea:focus {
                border-color: #00aa6c;
                box-shadow:
                    0 0 0 1px #00aa6c;
            }

            .stFormSubmitButton > button {
                width: 100%;
                background-color: #00aa6c;
                color: white;
                border: none;
                border-radius: 24px;
                min-height: 48px;
                font-size: 16px;
                font-weight: 700;
            }

            .stFormSubmitButton > button:hover {
                background-color: #008f5b;
                color: white;
                border: none;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )