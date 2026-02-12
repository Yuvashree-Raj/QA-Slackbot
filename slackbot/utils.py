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

ORGANIZATION RULES:
1. Identify major feature components from the product specification.
2. Organize test cases feature-wise.
3. Under each feature, group test cases into:
   - Positive Cases
   - Negative Cases
   - Edge Cases
   - Boundary Cases
4. Number test cases sequentially from 1 to 100 across all features.
5. Each test case must start with "Verify that".
6. One assertion per test case.
7. No explanations.
8. Follow this exact structure format:

OUTPUT FORMAT:

## 1. [Feature Name] (X test cases)

### Positive Cases
1. Verify that ...
2. Verify that ...

### Negative Cases
...

### Edge Cases
...

### Boundary Cases
...

Continue this structure for all features until 100 test cases are generated.

PRODUCT SPECIFICATION:
{feature_description}
"""



        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
