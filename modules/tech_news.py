from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime


def send_tech_news():
    today = datetime.now().strftime("%B %d, %Y")

    system = f"""You are a tech intelligence briefing bot for a curious non-expert.
Identify ONE real significant breakthrough in AI, science, or technology and
explain it clearly for a non-technical person in under 2 minutes of reading.
Never use asterisks, underscores, or markdown symbols. Plain text only.
Today's date: {today}"""

    prompt = f"""Give me today's most important breakthrough or development
in AI, technology, or science as of {today}.

Write in this format:

Good Morning - Tech Briefing
{today}

TODAY'S BREAKTHROUGH:
One sentence describing what happened.

WHY IT MATTERS:
Two to three sentences on the real world impact for regular people.

WHAT YOU SHOULD KNOW:
One to two sentences on the bigger picture or trend this fits into.

LEARN MORE:
One search term or website to learn more.

Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=1000)
    send_message(content)
