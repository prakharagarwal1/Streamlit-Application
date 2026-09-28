import streamlit as st

from components.header import render_header
from components.footer import render_footer
from components.sidebar import render_sidebar


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# Initialize Session State
# ---------------------------------------------------------
if "username" not in st.session_state:
    st.session_state.username = "Prakhar"


# ---------------------------------------------------------
# Common Header
# ---------------------------------------------------------
render_header()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
render_sidebar()


# ---------------------------------------------------------
# Navigation
# ---------------------------------------------------------
pages = {
    "Application": [
        st.Page(
            "pages/dashboard.py",
            title="Dashboard",
            icon="🏠",
            default=True
        ),
        st.Page(
            "pages/users.py",
            title="Users",
            icon="👥"
        ),
        st.Page(
            "pages/reports.py",
            title="Reports",
            icon="📊"
        ),
    ],
    "System": [
        st.Page(
            "pages/settings.py",
            title="Settings",
            icon="⚙️"
        ),
    ]
}

pg = st.navigation(pages)

pg.run()


# ---------------------------------------------------------
# Common Footer
# ---------------------------------------------------------
render_footer()