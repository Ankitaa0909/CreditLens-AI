import plotly.express as px
import plotly.graph_objects as go


def revenue_chart(df):

    fig = px.line(
        df,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Revenue"
    )

    return fig


def cashflow_chart(df):

    fig = px.bar(
        df,
        x="Month",
        y="Balance",
        title="Cashflow Trend"
    )

    return fig


def upi_chart(df):

    fig = px.line(
        df,
        x="Month",
        y="Amount",
        markers=True,
        title="UPI Collections"
    )

    return fig


def employee_chart(df):

    fig = px.bar(
        df,
        x="Month",
        y="Employees",
        title="Employee Growth"
    )

    return fig


def financial_gauge(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        title={"text": "Financial Health Score"},

        gauge={
            "axis": {"range": [0, 100]},

            "bar": {"color": "green"},

            "steps": [

                {"range": [0, 40], "color": "#ff4d4d"},

                {"range": [40, 70], "color": "#ffd633"},

                {"range": [70, 100], "color": "#66cc66"}

            ]

        }

    ))

    return fig
