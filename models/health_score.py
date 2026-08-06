import pandas as pd


class FinancialHealthScore:

    def __init__(self, gst_df, upi_df, epfo_df, bank_df):

        self.gst = gst_df
        self.upi = upi_df
        self.epfo = epfo_df
        self.bank = bank_df


    # ----------------------------
    # GST Compliance
    # ----------------------------

    def gst_score(self):

        filed = self.gst["GSTRFiled"].str.lower().eq("yes").sum()

        total = len(self.gst)

        return (filed / total) * 20


    # ----------------------------
    # Revenue Growth
    # ----------------------------

    def revenue_score(self):

        first = self.gst["Sales"].iloc[0]

        last = self.gst["Sales"].iloc[-1]

        growth = ((last-first)/first)*100

        if growth >=20:
            return 20

        elif growth >=10:
            return 15

        elif growth >=5:
            return 10

        return 5


    # ----------------------------
    # UPI Growth
    # ----------------------------

    def upi_score(self):

        first=self.upi["Amount"].iloc[0]

        last=self.upi["Amount"].iloc[-1]

        growth=((last-first)/first)*100

        if growth>=25:
            return 15

        elif growth>=15:
            return 12

        elif growth>=5:
            return 8

        return 4


    # ----------------------------
    # Employee Growth
    # ----------------------------

    def employee_score(self):

        first=self.epfo["Employees"].iloc[0]

        last=self.epfo["Employees"].iloc[-1]

        increase=last-first

        if increase>=5:
            return 15

        elif increase>=3:
            return 12

        elif increase>=1:
            return 8

        return 4


    # ----------------------------
    # Cash Flow
    # ----------------------------

    def cashflow_score(self):

        balance=self.bank["Balance"].mean()

        if balance>=70000:
            return 20

        elif balance>=50000:
            return 15

        elif balance>=30000:
            return 10

        return 5


    # ----------------------------
    # Final Score
    # ----------------------------

    def final_score(self):

        score=(
            self.gst_score()
            +self.revenue_score()
            +self.upi_score()
            +self.employee_score()
            +self.cashflow_score()
        )

        return round(score,2)
