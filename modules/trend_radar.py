from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime


def send_trend_radar():
    today = datetime.now().strftime("%B %d, %Y")
    week = datetime.now().isocalendar()[1]

    system = """You are a trend intelligence analyst identifying emerging trends
gaining momentum right now across technology, culture, business, health, and society.
Focus on trends relevant to someone living in Canada.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""Today is {today}, Week {week} of the year.
Identify exactly 3 trends gaining momentum right now that are not yet fully mainstream.

Write in this format:

TREND RADAR - Week {week}
{today}

TREND 1: [Name]
Category: Tech or Health or Work or Culture or Business
Signal: Early or Growing or Accelerating
What is happening: Two sentences.
Why it matters: One to two sentences on real world impact.
Your opportunity: One sentence on how you could benefit or prepare.

TREND 2: [Name]
Category: [...]
Signal: [...]
What is happening: Two sentences.
Why it matters: One to two sentences.
Your opportunity: One sentence.

TREND 3: [Name]
Category: [...]
Signal: [...]
What is happening: Two sentences.
Why it matters: One to two sentences.
Your opportunity: One sentence.

WILD CARD TO WATCH:
One unusual thing on the fringe that could become big in the next year.

Plain text only. No special characters. Total under 400 words."""

    content = ask_claude(prompt, system=system, max_tokens=1000)
    send_message(content)
