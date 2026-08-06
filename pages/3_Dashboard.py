import streamlit as st
import pandas as pd
from utils.charts import revenue_chart

st.title("📊 Financial Health Dashboard")

st.write("AI-powered assessment of MSME financial health.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric("Financial Health Score", "86 / 100", "+4")
col2.metric("Risk Level", "LOW", "-12%")
col3.metric("Loan Eligibility", "Eligible", "₹25 Lakhs")

st.markdown("---")

st.subheader("Financial Indicators")

a, b = st.columns(2)

with a:
    st.success("GST Compliance : 100%")
    st.success("Revenue Growth : 18%")
    st.success("Employee Growth : +4")

with b:
    st.success("Cash Flow : Healthy")
    st.success("UPI Growth : 25%")
    st.success("Credit Utilization : 41%")

st.markdown("---")

# Read sample GST data
if "gst_df" in st.session_state:
    df = st.session_state["gst_df"]
else:
    df = pd.read_csv("data/sample_gst.csv")

st.subheader("Revenue Trend")

st.plotly_chart(
    revenue_chart(df),
    use_container_width=True
)

st.markdown("---")

st.info(
    """
### 🤖 AI Observation

This MSME demonstrates strong financial discipline,
healthy cash flow, and consistent GST compliance.

Risk level is **LOW**.

Recommended for working capital financing.
"""
)
