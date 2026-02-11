import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")

HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"


def generate_testcases(feature_description):
    if not HF_TOKEN:
        return "HF_TOKEN not configured in environment variables."

    prompt = f"""
You are a professional QA engineer.

Generate structured frontend test cases.

STRICT RULES:
- Output ONLY in markdown table format.
- Do NOT explain anything.
- Follow this exact structure:

| Test Case ID | Test Case Title | Preconditions | Test Steps | Expected Result |
|--------------|----------------|--------------|------------|----------------|

Feature Description:
{feature_description}
"""

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 800,
            "temperature": 0.3,
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        result = response.json()

        if isinstance(result, list):
            return result[0].get("generated_text", "No output generated.")

        return str(result)

    except requests.exceptions.RequestException as e:
        return f"Error calling Hugging Face API: {str(e)}"
