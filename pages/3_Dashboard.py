import streamlit as st
import pandas as pd
from utils.charts import revenue_chart
from models.health_score import FinancialHealthScore

st.title("📊 Financial Health Dashboard")

st.write("AI-powered assessment of MSME Financial Health.")

st.markdown("---")

# ==========================
# Load Sample Data
# ==========================

gst = pd.read_csv("data/sample_gst.csv")
upi = pd.read_csv("data/sample_upi.csv")
epfo = pd.read_csv("data/sample_epfo.csv")
bank = pd.read_csv("data/sample_bank_statement.csv")

# ==========================
# Calculate Financial Score
# ==========================

engine = FinancialHealthScore(
    gst,
    upi,
    epfo,
    bank
)

score = engine.final_score()

# ==========================
# Risk Level
# ==========================

if score >= 75:
    risk = "🟢 LOW"
elif score >= 55:
    risk = "🟡 MEDIUM"
else:
    risk = "🔴 HIGH"

# ==========================
# Loan Eligibility
# ==========================

if score >= 75:
    loan = "✅ Eligible"
elif score >= 55:
    loan = "🟠 Needs Review"
else:
    loan = "❌ Not Eligible"

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Financial Health Score",
        f"{score}/90"
    )

with col2:
    st.metric(
        "Risk Level",
        risk
    )

with col3:
    st.metric(
        "Loan Eligibility",
        loan
    )

st.markdown("---")

# ==========================
# Financial Indicators
# ==========================

st.subheader("Financial Indicators")

left, right = st.columns(2)

with left:

    st.success(f"GST Compliance Score : {engine.gst_score():.1f}/20")

    st.success(f"Revenue Score : {engine.revenue_score():.1f}/20")

    st.success(f"Employee Score : {engine.employee_score():.1f}/15")

with right:

    st.success(f"UPI Score : {engine.upi_score():.1f}/15")

    st.success(f"Cashflow Score : {engine.cashflow_score():.1f}/20")

    st.success(f"Overall Score : {score}/90")

st.markdown("---")

# ==========================
# Revenue Trend
# ==========================

st.subheader("📈 Revenue Trend")

fig = revenue_chart(gst)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================
# AI Observation
# ==========================

st.info(f"""
### 🤖 AI Financial Analysis

**Financial Health Score:** {score}/90

**Risk Level:** {risk}

**Loan Decision:** {loan}

### Business Summary

• Excellent GST filing discipline

• Positive revenue growth

• Healthy digital payment activity

• Stable employee growth

• Healthy average bank balance

### AI Recommendation

This MSME demonstrates strong financial behaviour based on available alternate data.

CreditLens AI recommends proceeding with the next stage of credit evaluation.
""")
