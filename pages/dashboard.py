import streamlit as st
import pandas as pd


st.title("🏠 Dashboard")

st.write(
    f"Welcome back, **{st.session_state.username}**!"
)

st.markdown("---")


# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Users",
        value="1,245",
        delta="+12%"
    )

with col2:
    st.metric(
        label="Revenue",
        value="$45,230",
        delta="+8.5%"
    )

with col3:
    st.metric(
        label="Orders",
        value="856",
        delta="+15"
    )

with col4:
    st.metric(
        label="Conversion",
        value="4.8%",
        delta="+0.6%"
    )


st.markdown("---")


# ---------------------------------------------------------
# Chart Data
# ---------------------------------------------------------

data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],
        "Revenue": [
            12000,
            15000,
            18000,
            16000,
            21000,
            25000
        ]
    }
)

st.subheader("📈 Revenue")

st.line_chart(
    data.set_index("Month")
)


st.markdown("---")


# ---------------------------------------------------------
# Recent Activities
# ---------------------------------------------------------

st.subheader("🕒 Recent Activities")

activities = pd.DataFrame(
    {
        "User": [
            "John",
            "Sarah",
            "Mike",
            "David"
        ],
        "Action": [
            "Created order",
            "Updated profile",
            "Downloaded report",
            "Created account"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Completed",
            "Pending"
        ]
    }
)

st.dataframe(
    activities,
    use_container_width=True,
    hide_index=True
)