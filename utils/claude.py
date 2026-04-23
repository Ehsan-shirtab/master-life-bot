"""
utils/claude.py
Wrapper for calling Claude API (Anthropic).
"""

import os
import requests

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-20250514"


def ask_claude(prompt: str, system: str = None, max_tokens: int = 1000) -> str:
    """Send a prompt to Claude and return the text response."""
    if not ANTHROPIC_API_KEY:
        return "⚠️ ANTHROPIC_API_KEY not set."

    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }

    if system:
        body["system"] = system

    try:
        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=body,
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        return data["content"][0]["text"].strip()
    except Exception as e:
        return f"⚠️ Claude API error: {e}"
