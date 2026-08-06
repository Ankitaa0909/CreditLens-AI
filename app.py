import streamlit as st

st.set_page_config(
    page_title="CreditLens AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.logo("assets/logo.png")
st.sidebar.title("🏦 CreditLens AI")
st.sidebar.markdown("---")

st.write(
    "👈 Select a page from the sidebar to begin."
)
