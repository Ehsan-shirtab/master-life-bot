import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str, chat_id: str = None):
    target = chat_id or CHAT_ID
    if not TELEGRAM_TOKEN or not target:
        print("TELEGRAM_TOKEN or CHAT_ID not set")
        return

    # Remove markdown symbols that break Telegram
    clean = text.replace("*", "").replace("_", "").replace("`", "")

    chunks = [clean[i:i+3000] for i in range(0, len(clean), 3000)]

    for chunk in chunks:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": target,
            "text": chunk,
            "disable_web_page_preview": True,
        }
        try:
            r = requests.post(url, json=payload, timeout=10)
            r.raise_for_status()
        except Exception as e:
            print(f"Telegram send error: {e}")


def send_long_message(text: str, chat_id: str = None):
    send_message(text, chat_id=chat_id)
