from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime


def send_trend_radar():
    today = datetime.now().strftime("%B %d, %Y")
    week = datetime.now().isocalendar()[1]

    system = """You are a trend intelligence analyst identifying emerging trends
gaining momentum right now across technology, culture, business, health, and society.
Focus on trends relevant to someone living in Canada.
Never use asterisks, underscores, dashes as decoration, or any markdown.
Plain text only."""

    prompt = f"""Today is {today}, Week {week} of the year.
Identify exactly 3 trends gaining momentum right now that are not yet mainstream.
Also give one wild card trend at the end.

Write in plain paragraphs like this example:

TREND RADAR - Week {week}
{today}

TREND 1: Name of trend
Category: Tech
Signal: Growing
This trend is about... two sentences explaining what is happening.
This matters because... one sentence on real world impact.
Your opportunity: one sentence on how you could benefit.

TREND 2: Name of trend
Category: Health
Signal: Accelerating
This trend is about... two sentences explaining what is happening.
This matters because... one sentence on real world impact.
Your opportunity: one sentence on how you could benefit.

TREND 3: Name of trend
Category: Work
Signal: Early
This trend is about... two sentences explaining what is happening.
This matters because... one sentence on real world impact.
Your opportunity: one sentence on how you could benefit.

WILD CARD: Name of wild card trend
One to two sentences on something unusual that could become big.

Total response under 350 words. Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)
    send_message(content)
