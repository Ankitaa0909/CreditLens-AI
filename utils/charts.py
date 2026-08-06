import plotly.express as px

def revenue_chart(df):
    fig = px.line(
        df,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Revenue"
    )
    return fig
