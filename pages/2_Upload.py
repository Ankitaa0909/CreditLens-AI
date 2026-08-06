import streamlit as st
import pandas as pd

st.title("📂 Upload Financial Documents")

st.write(
    "Upload MSME financial datasets for AI-powered financial health assessment."
)

st.markdown("---")

gst = st.file_uploader(
    "Upload GST CSV",
    type=["csv"],
    key="gst"
)

upi = st.file_uploader(
    "Upload UPI CSV",
    type=["csv"],
    key="upi"
)

epfo = st.file_uploader(
    "Upload EPFO CSV",
    type=["csv"],
    key="epfo"
)

bank = st.file_uploader(
    "Upload Bank Statement CSV",
    type=["csv"],
    key="bank"
)

st.markdown("---")

if gst:
    df = pd.read_csv(gst)

    st.success("GST Uploaded Successfully")

    st.dataframe(df)

if upi:
    df = pd.read_csv(upi)

    st.success("UPI Uploaded Successfully")

    st.dataframe(df)

if epfo:
    df = pd.read_csv(epfo)

    st.success("EPFO Uploaded Successfully")

    st.dataframe(df)

if bank:
    df = pd.read_csv(bank)

    st.success("Bank Statement Uploaded Successfully")

    st.dataframe(df)
