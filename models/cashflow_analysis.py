class CashflowAnalysis:

    def __init__(self, bank_df):
        self.df = bank_df

    def average_balance(self):
        return round(self.df["Balance"].mean(), 2)

    def minimum_balance(self):
        return round(self.df["Balance"].min(), 2)

    def maximum_balance(self):
        return round(self.df["Balance"].max(), 2)

    def cashflow_trend(self):

        first = self.df["Balance"].iloc[0]
        last = self.df["Balance"].iloc[-1]

        if last > first:
            return "Increasing"

        elif last < first:
            return "Decreasing"

        return "Stable"
