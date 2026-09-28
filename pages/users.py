
import streamlit as st
import pandas as pd


st.title("👥 Users")

st.write("Manage application users.")

st.markdown("---")


# ---------------------------------------------------------
# Search
# ---------------------------------------------------------

search = st.text_input(
    "🔍 Search user",
    placeholder="Enter user name..."
)


# ---------------------------------------------------------
# Sample Data
# ---------------------------------------------------------

users = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4, 5],
        "Name": [
            "John Doe",
            "Sarah Smith",
            "Mike Johnson",
            "David Brown",
            "Emma Wilson"
        ],
        "Email": [
            "john@example.com",
            "sarah@example.com",
            "mike@example.com",
            "david@example.com",
            "emma@example.com"
        ],
        "Role": [
            "Admin",
            "User",
            "User",
            "Manager",
            "User"
        ],
        "Status": [
            "Active",
            "Active",
            "Inactive",
            "Active",
            "Active"
        ]
    }
)


# ---------------------------------------------------------
# Search Filter
# ---------------------------------------------------------

if search:
    users = users[
        users["Name"]
        .str.contains(search, case=False)
    ]


# ---------------------------------------------------------
# Display Users
# ---------------------------------------------------------

st.dataframe(
    users,
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# Add User
# ---------------------------------------------------------

st.markdown("---")

st.subheader("➕ Add User")

with st.form("add_user_form"):

    name = st.text_input("Name")

    email = st.text_input("Email")

    role = st.selectbox(
        "Role",
        ["User", "Manager", "Admin"]
    )

    submitted = st.form_submit_button(
        "Create User"
    )

    if submitted:

        if not name or not email:
            st.error("Name and Email are required.")

        else:
            st.success(
                f"User {name} created successfully!"
            )