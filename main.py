"""
Master Life Bot — main.py
One bot, 7 modules, smart daily schedule.
Trigger each module via: GET /run?module=MODULE_NAME&secret=YOUR_SECRET
"""

from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

from modules.tech_news import send_tech_news
from modules.skill_of_week import send_skill
from modules.second_brain import handle_second_brain, send_second_brain
from modules.trend_radar import send_trend_radar
from modules.book_summary import send_book_summary
from modules.language import send_language_lesson
from modules.analytics import send_analytics

load_dotenv()

app = Flask(__name__)

SECRET = os.getenv("BOT_SECRET", "changeme")

MODULES = {
    "tech_news":     send_tech_news,
    "skill":         send_skill,
    "second_brain":  send_second_brain,
    "trend_radar":   send_trend_radar,
    "book_summary":  send_book_summary,
    "language":      send_language_lesson,
    "analytics":     send_analytics,
}



@app.route("/")
def index():
    return jsonify({"status": "Master Life Bot is alive 🤖"}), 200
@app.route("/health")
def health():
    return "OK", 200

@app.route("/run")
def run_module():
    secret = request.args.get("secret", "")
    if secret != SECRET:
        return jsonify({"error": "Unauthorized"}), 401

    module = request.args.get("module", "")
    if module not in MODULES:
        return jsonify({"error": f"Unknown module '{module}'. Available: {list(MODULES.keys())}"}), 400

    try:
        MODULES[module]()
        return jsonify({"status": "ok", "module": module}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    """
    Receives messages from Telegram.
    Used by Second Brain module — user forwards links/articles to the bot.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"ok": True})

    try:
        message = data.get("message", {})
        text = message.get("text", "")
        chat_id = message.get("chat", {}).get("id")

        if text and chat_id:
            handle_second_brain(text, chat_id)
    except Exception as e:
        print(f"Webhook error: {e}")

    return jsonify({"ok": True})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
