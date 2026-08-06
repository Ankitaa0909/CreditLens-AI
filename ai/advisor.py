from ai.gemini import ask_gemini
from ai.prompts import FINANCIAL_ANALYSIS_PROMPT


def generate_ai_advice(
    score,
    gst_score,
    revenue_score,
    upi_score,
    cashflow_score,
    employee_score,
    risk,
    loan,
):
    """
    Generate AI financial analysis.
    """

    prompt = FINANCIAL_ANALYSIS_PROMPT.format(
        score=score,
        gst_score=gst_score,
        revenue_score=revenue_score,
        upi_score=upi_score,
        cashflow_score=cashflow_score,
        employee_score=employee_score,
        risk=risk,
        loan=loan,
    )

    return ask_gemini(prompt)
