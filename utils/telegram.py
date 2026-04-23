"""
utils/telegram.py
Send messages to Telegram with Markdown formatting.
"""

import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str, chat_id: str = None, parse_mode: str = "Markdown"):
    """Send a message to Telegram."""
    target = chat_id or CHAT_ID
    if not TELEGRAM_TOKEN or not target:
        print("⚠️  TELEGRAM_TOKEN or CHAT_ID not set")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": target,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": False,
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"Telegram send error: {e}")


def send_long_message(text: str, chat_id: str = None):
    """Split and send messages longer than 4096 chars (Telegram limit)."""
    target = chat_id or CHAT_ID
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    for chunk in chunks:
        send_message(chunk, chat_id=target)
