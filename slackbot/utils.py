import os
import google.generativeai as genai

# Load API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use lightweight free-tier friendly model
MODEL_NAME = "gemini-1.5-flash"


def generate_testcases(feature_description):
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
You are a professional QA engineer.

Generate structured frontend test cases.

STRICT RULES:
- Output ONLY in markdown table format.
- Do NOT explain anything.

| Test Case ID | Test Case Title | Preconditions | Test Steps | Expected Result |
|--------------|----------------|--------------|------------|----------------|

Feature Description:
{feature_description}
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
