
import streamlit as st


def render_sidebar():
    st.sidebar.markdown(
        """
        # 🚀 My App
        """
    )

    st.sidebar.markdown("---")

    st.sidebar.write(
        f"👤 Logged in as: **{st.session_state.username}**"
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("Quick Settings")

    notifications = st.sidebar.checkbox(
        "Enable notifications",
        value=True
    )

    if notifications:
        st.sidebar.success("Notifications ON")
    else:
        st.sidebar.warning("Notifications OFF")

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Use the navigation menu above to move between pages."
    )