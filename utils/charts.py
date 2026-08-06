import plotly.express as px

def revenue_chart(df):

    fig = px.line(
        df,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Revenue"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    return fig
