GST_COLUMNS = [
    "Month",
    "Sales",
    "GST",
    "GSTRFiled"
]

UPI_COLUMNS = [
    "Month",
    "Transactions",
    "Amount"
]

EPFO_COLUMNS = [
    "Month",
    "Employees"
]

BANK_COLUMNS = [
    "Month",
    "Balance"
]


def validate_columns(df, required_columns):

    missing = []

    for col in required_columns:

        if col not in df.columns:
            missing.append(col)

    return missing
