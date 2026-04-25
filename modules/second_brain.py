import re
from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


def is_url(text: str) -> bool:
    return bool(re.match(r'https?://', text.strip()))


def handle_second_brain(text: str, chat_id: str):
    text = text.strip()

    if len(text) < 10 and not is_url(text):
        send_message(
            "Send me a URL to summarize, or any topic to explore. "
            "Example: 'quantum computing' or 'https://bbc.com/article'",
            chat_id=chat_id
        )
        return

    if is_url(text):
        _summarize_url(text, chat_id)
    else:
        _explore_topic(text, chat_id)


def _summarize_url(url: str, chat_id: str):
    send_message("Got it! Summarizing for your Second Brain...", chat_id=chat_id)

    system = """You are a Second Brain assistant. Extract the most valuable 
knowledge from any URL or article shared. Be concise and insightful.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""The user shared this URL: {url}

Write a Second Brain summary in this format:

SECOND BRAIN CAPTURE

WHAT IS THIS:
One sentence describing what this content is.

KEY IDEAS:
1. [Idea 1]
2. [Idea 2]
3. [Idea 3]
4. [Idea 4]

MOST IMPORTANT INSIGHT:
The single most valuable takeaway.

QUESTION TO THINK ABOUT:
One thought-provoking question this content raises.

TAGS: [3-5 topic tags]

Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)
    send_message(content, chat_id=chat_id)


def _explore_topic(text: str, chat_id: str):
    send_message("Exploring this for your Second Brain...", chat_id=chat_id)

    system = """You are a Second Brain research assistant.
Help the user understand and capture knowledge about any topic.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""The user wants to explore: {text}

Write a Second Brain entry in this format:

SECOND BRAIN - {text.upper()[:40]}

OVERVIEW:
2 to 3 sentences explaining this topic clearly.

KEY IDEAS:
1. [Most important concept 1]
2. [Most important concept 2]
3. [Most important concept 3]

REAL WORLD CONNECTION:
How this topic connects to everyday life.

BEST RESOURCE TO LEARN MORE:
One specific book, course, or website.

TAGS: [3-5 topic tags]

Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)
    send_message(content, chat_id=chat_id)


def send_second_brain():
    today = datetime.now().strftime("%B %d, %Y")
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
surprising, counterintuitive, or immediately useful.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""Today is {today}. Find ONE fascinating concept or idea from: {topic}

Write in this format:

SECOND BRAIN CAPTURE - {today}

IDEA NAME: [Give it a compelling name]

WHAT IS IT:
2 to 3 sentences explaining the idea clearly.

THE SURPRISING PART:
The counterintuitive or fascinating aspect most people do not know.

HOW TO USE THIS:
One practical way to apply this idea in real life.

LEARN MORE:
One book, website, or search term to explore further.

Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)
    send_message(content)
