import pandas as pd

def clean_dataframe(df):
    """
    Basic preprocessing
    """

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(0)

    return df


def convert_dates(df, column):
    """
    Convert a column into datetime
    """

    if column in df.columns:
        df[column] = pd.to_datetime(df[column])

    return df
