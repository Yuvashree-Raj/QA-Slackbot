import os
import google.generativeai as genai

# Load API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use lightweight free-tier friendly model

MODEL_NAME = "gemini-flash-latest"


def generate_testcases(feature_description):
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
You are a senior QA engineer.

TASK:
Generate exactly 100 high-priority Manual Frontend test cases.

FOCUS:
- Edge cases
- Negative scenarios
- Boundary conditions
- Permission violations
- Validation failures
- Critical user flows

RULES:
- Start every test case with "Verify that"
- One assertion per test case
- No explanations
- No markdown formatting
- No summary
- Number sequentially from 1 to 100
- Organize by feature component

DISTRIBUTION:
- ~35 Positive
- ~35 Negative
- ~20 Edge
- ~10 Boundary

PRODUCT SPECIFICATION:
{feature_description}
"""


        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
