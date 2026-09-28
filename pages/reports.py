import streamlit as st
import pandas as pd


st.title("📊 Reports")

st.write(
    "Generate and view application reports."
)

st.markdown("---")


# ---------------------------------------------------------
# Filters
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    report_type = st.selectbox(
        "Report Type",
        [
            "Sales",
            "Users",
            "Revenue"
        ]
    )

with col2:

    period = st.selectbox(
        "Period",
        [
            "Last 7 Days",
            "Last 30 Days",
            "Last 90 Days"
        ]
    )


st.markdown("---")


# ---------------------------------------------------------
# Report Data
# ---------------------------------------------------------

report_data = pd.DataFrame(
    {
        "Month": [
            "January",
            "February",
            "March",
            "April",
            "May"
        ],
        "Orders": [
            120,
            150,
            180,
            210,
            250
        ],
        "Revenue": [
            12000,
            15000,
            18000,
            21000,
            25000
        ]
    }
)


st.subheader(
    f"{report_type} Report"
)

st.dataframe(
    report_data,
    use_container_width=True,
    hide_index=True
)


st.subheader("📈 Report Chart")

st.bar_chart(
    report_data.set_index("Month")[
        "Revenue"
    ]
)


# ---------------------------------------------------------
# Download
# ---------------------------------------------------------

csv = report_data.to_csv(
    index=False
)

st.download_button(
    label="⬇️ Download CSV",
    data=csv,
    file_name="report.csv",
    mime="text/csv"
)