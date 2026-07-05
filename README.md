# CreditLens AI – MSME Financial Health Copilot

<p align="center">
  <img src="assets/logo.png" alt="CreditLens AI Logo" width="180">
</p>

<p align="center">
  <strong>AI-Powered Financial Health Assessment Platform for MSMEs</strong><br>
  Built for <strong>IDBI Innovate Hackathon 2026</strong>
</p>

---

## Overview

CreditLens AI is an AI-powered Financial Health Copilot designed to help banks assess the creditworthiness of **New-to-Credit (NTC)** and **New-to-Bank (NTB)** MSMEs using alternate financial data instead of relying solely on traditional financial statements.

The platform aggregates financial information from multiple sources such as **GST, UPI, Bank Statements, EPFO**, and **Account Aggregator (AA)** data to generate a multidimensional Financial Health Score, provide AI-driven insights, recommend suitable loan products, and enable explainable lending decisions.

---

## Problem Statement

**Problem Statement 3 – Financial Health Score**

Traditional MSME credit evaluation depends heavily on audited financial statements and historical credit records, making it difficult for many deserving businesses to obtain financing.

CreditLens AI addresses this challenge by leveraging alternate financial data to provide:

- Near real-time credit assessment
- Explainable Financial Health Score
- AI-powered credit recommendations
- Loan readiness evaluation
- Improved financial inclusion

---

# Key Features

- Financial Health Score (0–100)
- AI Credit Officer (LLM-powered assistant)
- Cash Flow Analysis
- GST Compliance Analysis
- UPI Transaction Insights
- Business Growth Analysis
- Loan Readiness Score
- Personalized Loan Recommendations
- Risk Radar Dashboard
- What-If Financial Simulator
- Banker Portfolio Dashboard
- Explainable AI Recommendations

---

# System Workflow

```
MSME User
      │
      ▼
Upload Financial Documents
(GST / UPI / Bank Statement / EPFO)
      │
      ▼
Data Processing Engine
      │
      ▼
Financial Health Engine
      │
      ├── Cash Flow Analysis
      ├── Compliance Analysis
      ├── Growth Analysis
      ├── Risk Assessment
      └── Loan Readiness
      │
      ▼
AI Recommendation Engine
      │
      ▼
Interactive Dashboard
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI | Google Gemini API |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Visualization | Plotly |
| Database | SQLite |
| Deployment | AWS EC2 |
| Version Control | Git & GitHub |

---

# Folder Structure

```
creditlens-ai/

│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── .gitignore
│
├── ai/
│   ├── gemini.py
│   └── prompts.py
│
├── data/
│   ├── sample_gst.csv
│   ├── sample_upi.csv
│   ├── sample_bank_statement.csv
│   └── sample_epfo.csv
│
├── models/
│   ├── health_score.py
│   ├── recommendation.py
│   └── risk_prediction.py
│
├── pages/
│   ├── Dashboard.py
│   ├── Upload.py
│   ├── LoanAdvisor.py
│   ├── RiskAnalysis.py
│   └── Simulator.py
│
├── utils/
│   ├── preprocessing.py
│   ├── parser.py
│   └── charts.py
│
├── assets/
│   └── logo.png
│
└── screenshots/
```

---

# Financial Health Score Model

The Financial Health Score is calculated using multiple business indicators.

| Parameter | Weight |
|------------|---------|
| Cash Flow | 30% |
| GST Compliance | 20% |
| Business Growth | 20% |
| Digital Transactions | 15% |
| Liquidity | 10% |
| Business Stability | 5% |

Final Score = Weighted Average of all financial indicators.

---

# AI Modules

## AI Credit Officer

Provides natural language explanations for:

- Why a business received a particular score
- Risk factors
- Loan eligibility
- Suggestions to improve financial health

---

## Loan Recommendation Engine

Recommends suitable loan products based on:

- Financial Health Score
- Repayment Capacity
- Cash Flow Stability
- Business Growth
- Compliance History

---

## What-If Financial Simulator

Allows bankers to simulate different business scenarios.

Examples:

- Increase revenue by 15%
- Delay GST filing
- Increase expenses
- Hire more employees
- Reduce UPI collections

The platform recalculates the Financial Health Score instantly.

---

## Risk Radar

The system evaluates:

- Compliance Risk
- Liquidity Risk
- Cash Flow Risk
- Business Stability
- Digital Adoption
- Repayment Capacity

---

# Dashboard Modules

### MSME Dashboard

- Financial Health Score
- Revenue Trends
- Expense Analysis
- Cash Flow
- Loan Readiness
- AI Insights

### Banker Dashboard

- Portfolio Overview
- Risk Segmentation
- Loan Recommendations
- MSME Rankings
- Credit Health Distribution

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/creditlens-ai.git

cd creditlens-ai
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

# Future Scope

- Account Aggregator (AA) Integration
- OCEN Integration
- ULI Integration
- AI Fraud Detection
- Real-Time Banking APIs
- Multi-language Support
- OCR for Financial Documents
- Automated Credit Underwriting
- Credit Monitoring Alerts

---

# Demo

The demonstration follows this workflow:

1. Upload MSME financial data
2. Generate Financial Health Score
3. View AI-generated recommendations
4. Simulate business scenarios
5. Receive personalized loan suggestions
6. Monitor risk using the Banker Dashboard

---

# Disclaimer

This project has been developed solely for the **IDBI Innovate Hackathon 2026**.

The financial datasets used are simulated for demonstration purposes only.

No real customer banking information is stored or processed.

---

# Authors

**<Your Name>**

Cloud Engineer | AI Enthusiast | DevOps Engineer

---

# Acknowledgements

- IDBI Bank
- Hack2Skill
- Google Gemini API
- Streamlit
- Plotly
- Scikit-learn
- Pandas
- AWS

---

## License

This project is licensed under the MIT License.

---
**Made with ❤️ for IDBI Innovate Hackathon 2026**
