"""
utils/ai.py
AI wrapper using Google Gemini API (FREE — no credit card needed).

Get your free API key at:
https://aistudio.google.com/app/apikey
(Sign in with Google → Create API Key → Copy it)

Free tier limits (very generous):
- Gemini 2.5 Flash: 15 requests/min, 1,500 requests/day, 1M tokens/min
- More than enough for all 7 bot modules combined
"""

import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Using Gemini 2.5 Flash — fastest, free, and excellent quality
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent"
)


def ask_claude(prompt: str, system: str = None, max_tokens: int = 1000) -> str:
    """
    Drop-in replacement for the old Claude API call.
    Same function name so no other files need to change.
    Uses Google Gemini 2.5 Flash (free tier).
    """
    if not GEMINI_API_KEY:
        return "⚠️ GEMINI_API_KEY not set. Get your free key at https://aistudio.google.com/app/apikey"

    # Combine system prompt + user prompt (Gemini handles them together)
    full_prompt = f"{system}\n\n{prompt}" if system else prompt

    headers = {"Content-Type": "application/json"}

    body = {
        "contents": [
            {
                "parts": [{"text": full_prompt}]
            }
        ],
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "temperature": 0.7,
        }
    }

    try:
        r = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=body,
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response else "unknown"
        if status == 400:
            return "⚠️ Gemini API error: Bad request. Check your prompt."
        elif status == 403:
            return "⚠️ Gemini API error: Invalid API key. Check GEMINI_API_KEY in your .env"
        elif status == 429:
            return "⚠️ Gemini API: Rate limit hit. Free tier allows 15 requests/min — try again shortly."
        return f"⚠️ Gemini API HTTP error {status}: {e}"

    except Exception as e:
        return f"⚠️ Gemini API error: {e}"
