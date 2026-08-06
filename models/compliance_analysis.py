class ComplianceAnalysis:

    def __init__(self, gst_df):
        self.df = gst_df

    def filing_percentage(self):

        filed = self.df["GSTRFiled"].str.lower().eq("yes").sum()

        total = len(self.df)

        return round((filed / total) * 100, 2)

    def compliance_level(self):

        percentage = self.filing_percentage()

        if percentage >= 95:
            return "Excellent"

        elif percentage >= 80:
            return "Good"

        elif percentage >= 60:
            return "Average"

        else:
            return "Poor"
