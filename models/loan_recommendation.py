class LoanRecommendation:

    @staticmethod
    def recommend(score):

        if score >= 85:

            return {

                "loan": "Working Capital Loan",

                "amount": "₹25,00,000",

                "interest": "9.2%",

                "tenure": "5 Years"

            }

        elif score >= 70:

            return {

                "loan": "Business Expansion Loan",

                "amount": "₹15,00,000",

                "interest": "10.5%",

                "tenure": "4 Years"

            }

        elif score >= 55:

            return {

                "loan": "Micro Enterprise Loan",

                "amount": "₹5,00,000",

                "interest": "11.8%",

                "tenure": "3 Years"

            }

        else:

            return {

                "loan": "Not Eligible",

                "amount": "-",

                "interest": "-",

                "tenure": "-"

            }
