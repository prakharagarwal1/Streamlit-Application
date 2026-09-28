import pandas as pd


def get_users():

    return pd.DataFrame(
        {
            "ID": [1, 2, 3],
            "Name": [
                "John",
                "Sarah",
                "Mike"
            ],
            "Role": [
                "Admin",
                "User",
                "Manager"
            ]
        }
    )


def get_sales():

    return pd.DataFrame(
        {
            "Month": [
                "Jan",
                "Feb",
                "Mar",
                "Apr"
            ],
            "Sales": [
                10000,
                15000,
                18000,
                22000
            ]
        }
    )