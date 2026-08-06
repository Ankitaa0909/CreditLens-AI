class RiskPrediction:

    @staticmethod
    def predict(score):

        if score >= 80:
            return {
                "risk": "Low",
                "color": "green",
                "probability": "8%"
            }

        elif score >= 60:
            return {
                "risk": "Medium",
                "color": "orange",
                "probability": "28%"
            }

        else:
            return {
                "risk": "High",
                "color": "red",
                "probability": "65%"
            }
