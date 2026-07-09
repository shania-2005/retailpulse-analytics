import pandas as pd


def clean_data(df):
    """
    Clean Online Retail dataset.
    """

    df = df.copy()

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove missing values
    df = df.dropna(
        subset=["Description", "Customer ID"]
    )

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove invalid quantity
    df = df[df["Quantity"] > 0]

    # Remove invalid price
    df = df[df["Price"] > 0]

    # Remove cancelled invoices
    df = df[
        ~df["Invoice"].astype(str).str.startswith("C")
    ]

    return df