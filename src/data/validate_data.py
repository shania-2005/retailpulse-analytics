import pandas as pd


def validate_data(df):
    """
    Validate cleaned dataset.
    """

    report = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Negative Quantity": (df["Quantity"] <= 0).sum(),
        "Negative Price": (df["Price"] <= 0).sum(),
        "Negative Revenue": (df["Revenue"] <= 0).sum(),
        "Unique Customers": df["Customer ID"].nunique(),
        "Unique Products": df["StockCode"].nunique(),
        "Unique Invoices": df["Invoice"].nunique()
    }

    return pd.DataFrame(
        report.items(),
        columns=["Metric", "Value"]
    )