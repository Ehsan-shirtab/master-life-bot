"""
modules/second_brain.py
Module 3: Second Brain
Two modes:
  A) User forwards a link or text to the bot via Telegram → it summarizes + extracts insights
  B) Daily at 9:30 PM → bot auto-finds one valuable article/idea and summarizes it

The bot is smart: it detects if the message is a URL, a topic, or free text
and handles each appropriately.
"""

import re
from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime


def is_url(text: str) -> bool:
    return bool(re.match(r'https?://', text.strip()))


def handle_second_brain(text: str, chat_id: str):
    """
    Called from webhook when user sends a message to the bot.
    Detects what the user sent and responds accordingly.
    """
    text = text.strip()

    # Ignore simple greetings
    if len(text) < 10 and not is_url(text):
        send_message(
            "👋 Send me:\n"
            "• A *URL* to summarize an article\n"
            "• A *topic* to explore (e.g. 'quantum computing')\n"
            "• Any *text* to extract key ideas from",
            chat_id=chat_id
        )
        return

    if is_url(text):
        _summarize_url(text, chat_id)
    else:
        _explore_topic(text, chat_id)


def _summarize_url(url: str, chat_id: str):
    """Summarize a URL the user sent."""
    send_message("🧠 Got it! Summarizing for your Second Brain...", chat_id=chat_id)

    system = """You are a Second Brain assistant. When given a URL or article,
extract the most valuable knowledge from it. Be concise and insightful."""

    prompt = f"""The user shared this URL: {url}

Please provide a Second Brain summary in this EXACT format:

🔗 *SECOND BRAIN CAPTURE*

📌 *WHAT IS THIS?*
[One sentence describing what this content is]

💎 *KEY IDEAS* (max 4 bullet points)
• [Idea 1]
• [Idea 2]
• [Idea 3]
• [Idea 4]

🧠 *MOST IMPORTANT INSIGHT*
[The single most valuable takeaway]

❓ *QUESTION TO THINK ABOUT*
[One thought-provoking question this content raises]

🏷️ *TAGS*
[3-5 topic tags like: #productivity #AI #mindset]

Keep it under 200 words total."""

    content = ask_claude(prompt, system=system, max_tokens=600)
    send_message(content, chat_id=chat_id)


def _explore_topic(text: str, chat_id: str):
    """User sent a topic or free text — explore and extract ideas."""
    send_message("🔍 Exploring this for your Second Brain...", chat_id=chat_id)

    system = """You are a Second Brain research assistant. 
Help the user understand and capture knowledge about any topic they mention."""

    prompt = f"""The user wants to explore or capture ideas about: "{text}"

Provide a Second Brain entry in this EXACT format:

🧠 *SECOND BRAIN — {text.upper()[:40]}*

📖 *OVERVIEW*
[2-3 sentences explaining this topic clearly]

💎 *KEY IDEAS*
• [Most important concept 1]
• [Most important concept 2]  
• [Most important concept 3]

🌍 *REAL WORLD CONNECTION*
[How this topic connects to everyday life]

📚 *BEST RESOURCE TO LEARN MORE*
[One specific book, course, or website]

🏷️ *TAGS*
[3-5 topic tags]

Keep it practical and under 200 words."""

    content = ask_claude(prompt, system=system, max_tokens=600)
    send_message(content, chat_id=chat_id)


def send_second_brain():
    """
    Called by cron at 9:30 PM daily.
    Bot auto-finds one valuable idea and sends it proactively.
    """
    today = datetime.now().strftime("%B %d, %Y")

    # Rotate through interesting topic areas by day of week
    from datetime import date
    day = date.today().weekday()
    topics = [
        "psychology and human behavior",
        "future of work and technology",
        "health and longevity science",
        "economics and how money works",
        "philosophy and decision making",
        "nature and environmental science",
        "history lessons relevant to today",
    ]
    topic = topics[day]

    system = """You are a Second Brain curator. Every day you find one 
fascinating, practical idea worth knowing. You focus on ideas that are 
surprising, counterintuitive, or immediately useful."""

    prompt = f"""Today is {today}. Find ONE fascinating concept or idea from the domain of: {topic}

Format EXACTLY:

🌙 *TONIGHT'S SECOND BRAIN CAPTURE*
_{today}_

💡 *IDEA: [Give it a compelling name]*

📖 *WHAT IS IT?*
[2-3 sentences explaining the idea clearly]

🤯 *THE SURPRISING PART*
[The counterintuitive or fascinating aspect most people don't know]

🛠️ *HOW TO USE THIS*
[One practical way to apply this idea in real life]

📚 *SOURCE / LEARN MORE*
[Where to learn more about this]

Keep it under 220 words. Make it genuinely interesting."""

    content = ask_claude(prompt, system=system, max_tokens=600)
    send_message(content)
