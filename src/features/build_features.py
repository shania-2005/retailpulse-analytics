def build_features(df):
    """
    Create new features for ML models.
    """

    df = df.copy()

    # Revenue
    df["Revenue"] = (
        df["Quantity"] * df["Price"]
    )

    # Time Features
    df["Year"] = df["InvoiceDate"].dt.year

    df["Month"] = df["InvoiceDate"].dt.month

    df["MonthName"] = df["InvoiceDate"].dt.month_name()

    df["Day"] = df["InvoiceDate"].dt.day

    df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

    df["Hour"] = df["InvoiceDate"].dt.hour

    df["Quarter"] = df["InvoiceDate"].dt.quarter

    # Weekend
    df["IsWeekend"] = (
        df["DayOfWeek"]
        .isin(["Saturday", "Sunday"])
        .astype(int)
    )

    # Basket Size
    basket_size = (
        df.groupby("Invoice")["Quantity"]
        .sum()
    )

    df["BasketSize"] = (
        df["Invoice"]
        .map(basket_size)
    )

    # Order Value
    order_value = (
        df.groupby("Invoice")["Revenue"]
        .sum()
    )

    df["OrderValue"] = (
        df["Invoice"]
        .map(order_value)
    )

    return df