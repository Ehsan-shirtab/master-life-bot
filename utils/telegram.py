import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str, chat_id: str = None):
    target = chat_id or CHAT_ID
    if not TELEGRAM_TOKEN or not target:
        print("TELEGRAM_TOKEN or CHAT_ID not set")
        return

    # Clean any markdown symbols
    clean = text.replace("*", "").replace("`", "")

    # Split into chunks of 3800 characters at paragraph boundaries
    chunks = []
    while len(clean) > 3800:
        # Find the last paragraph break before 3800 chars
        split_at = clean.rfind("\n\n", 0, 3800)
        if split_at == -1:
            # No paragraph break found, split at last newline
            split_at = clean.rfind("\n", 0, 3800)
        if split_at == -1:
            # No newline found, hard split
            split_at = 3800
        chunks.append(clean[:split_at].strip())
        clean = clean[split_at:].strip()

    chunks.append(clean)

    # Send each chunk
    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
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
            print(f"Telegram send error on chunk {i+1}: {e}")


def send_long_message(text: str, chat_id: str = None):
    send_message(text, chat_id=chat_id)
