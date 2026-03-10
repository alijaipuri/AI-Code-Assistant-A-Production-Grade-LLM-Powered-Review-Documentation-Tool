import httpx
from .config import GROQ_API_KEY, MODEL

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

async def call_llm(prompt):

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_URL, headers=headers, json=payload)
        data = response.json()

    return data["choices"][0]["message"]["content"]


async def analyze_code(code):

    prompt = f"""
You are a senior software engineer.

Review the following Python code for:
- bugs
- inefficiencies
- style violations
- improvements

Code:
{code}
"""

    return await call_llm(prompt)


async def generate_docstring(code):

    prompt = f"""
Generate clean Python docstrings for the following function:

{code}
"""

    return await call_llm(prompt)
