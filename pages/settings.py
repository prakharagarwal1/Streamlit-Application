import streamlit as st


st.title("⚙️ Settings")

st.write(
    "Configure your application."
)

st.markdown("---")


# ---------------------------------------------------------
# Profile
# ---------------------------------------------------------

st.subheader("👤 Profile")

name = st.text_input(
    "Username",
    value=st.session_state.username
)

if st.button("Save Profile"):

    st.session_state.username = name

    st.success(
        "Profile updated successfully!"
    )


# ---------------------------------------------------------
# Application Settings
# ---------------------------------------------------------

st.subheader("🔧 Application Settings")

language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi"
    ]
)

auto_refresh = st.checkbox(
    "Enable auto refresh",
    value=True
)


if st.button("Save Settings"):

    st.success(
        "Settings saved successfully!"
    )


# ---------------------------------------------------------
# Debug Information
# ---------------------------------------------------------

st.markdown("---")

with st.expander("Session State"):

    st.write(
        dict(st.session_state)
    )