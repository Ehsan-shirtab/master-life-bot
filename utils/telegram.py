"""
utils/telegram.py
Send messages to Telegram with Markdown formatting.
"""
import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str, chat_id: str = None, parse_mode: str = "Markdown"):
    target = chat_id or CHAT_ID
    if not TELEGRAM_TOKEN or not target:
        print("⚠️  TELEGRAM_TOKEN or CHAT_ID not set")
        return

    # Split long messages automatically
    chunks = [text[i:i+3000] for i in range(0, len(text), 3000)]
    
    for chunk in chunks:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": target,
            "text": chunk,
            "parse_mode": parse_mode,
            "disable_web_page_preview": False,
        }
        try:
            r = requests.post(url, json=payload, timeout=10)
            r.raise_for_status()
        except Exception as e:
            # Try again without Markdown if formatting caused the error
            try:
                payload["parse_mode"] = "HTML"
                requests.post(url, json=payload, timeout=10)
            except Exception as e2:
                print(f"Telegram send error: {e2}")


def send_long_message(text: str, chat_id: str = None):
    send_message(text, chat_id=chat_id)
