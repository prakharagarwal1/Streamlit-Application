import streamlit as st


def render_header():
    st.markdown(
        """
        <style>
            .app-header {
                padding: 10px 0 20px 0;
                border-bottom: 1px solid #ddd;
                margin-bottom: 25px;
            }

            .app-header-title {
                font-size: 30px;
                font-weight: 700;
                margin: 0;
            }

            .app-header-subtitle {
                font-size: 15px;
                color: gray;
                margin-top: 5px;
            }
        </style>

        <div class="app-header">
            <div class="app-header-title">
                🚀 My Streamlit Application
            </div>

            <div class="app-header-subtitle">
                Admin dashboard and reporting system
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )