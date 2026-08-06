import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt):
    """
    Send prompt to Gemini and return response.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
