import pandas as pd

def load_file(uploaded_file):
    """
    Load CSV or Excel file into a Pandas DataFrame.
    """

    if uploaded_file is None:
        return None

    filename = uploaded_file.name.lower()

    if filename.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        return pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel.")
