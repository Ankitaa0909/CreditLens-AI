import streamlit as st

st.title("🏦 CreditLens AI")

st.subheader("Empowering MSMEs with AI-driven Financial Health Assessment")

st.markdown("---")

st.write("""
CreditLens AI is an AI-powered platform that helps banks assess MSME financial health using alternative data sources.

The platform analyzes:

- GST Transactions
- UPI Payments
- Bank Statements
- EPFO Data

Instead of relying only on traditional financial statements, CreditLens AI provides a multidimensional Financial Health Score.
""")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Assessment Accuracy", "95%")
col2.metric("Analysis Time", "<5 sec")
col3.metric("Data Sources", "6")
col4.metric("Digital Process", "100%")

st.markdown("---")

st.header("✨ Platform Features")

c1, c2 = st.columns(2)

with c1:

    st.success("📊 Financial Health Score")

    st.success("📈 Cash Flow Analysis")

    st.success("💳 Loan Recommendation")

with c2:

    st.success("🤖 AI Business Advisor")

    st.success("⚠ Risk Prediction")

    st.success("🔮 What-if Simulator")

st.markdown("---")

st.header("How it Works")

st.write("1️⃣ Upload MSME Financial Data")

st.write("⬇")

st.write("2️⃣ AI Analysis")

st.write("⬇")

st.write("3️⃣ Financial Health Score")

st.write("⬇")

st.write("4️⃣ Loan Recommendation")

st.markdown("---")

st.caption("Built for IDBI Innovate Hackathon 2026")
