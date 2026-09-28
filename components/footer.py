
import streamlit as st


def render_footer():
    st.markdown(
        """
        <hr>

        <div style="
            text-align: center;
            color: gray;
            font-size: 14px;
            padding: 15px;
        ">
            © 2026 My Streamlit Application |
            Built with Python + Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )