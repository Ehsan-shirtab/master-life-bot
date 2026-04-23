"""
modules/trend_radar.py
Module 4: Trend Radar
Sent every Monday at 8:00 AM Vancouver time.

What it does:
- Identifies 3 trends growing RIGHT NOW across tech, society, business, culture
- Explains each trend + why it matters + what opportunity it might create
- Helps you spot things 6-12 months before they go mainstream
"""

from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime


def send_trend_radar():
    today = datetime.now().strftime("%B %d, %Y")
    week = datetime.now().isocalendar()[1]

    system = """You are a trend intelligence analyst. Your job is to identify 
emerging trends that are just starting to gain momentum — not things that are 
already mainstream. You look across: technology, culture, business, health, 
work, and society. You focus on trends that a regular person in Canada could 
actually act on or benefit from knowing."""

    prompt = f"""Today is {today} (Week {week} of the year).

Identify exactly 3 trends that are gaining significant momentum RIGHT NOW. 
These should be things that are growing fast but not yet fully mainstream.

Format EXACTLY:

📡 *TREND RADAR — Week {week}*
_{today}_

━━━━━━━━━━━━━━━━━

📈 *TREND 1: [Name]*
🏷️ Category: [Tech / Health / Work / Culture / Business]
📊 Signal strength: [Early 🟡 / Growing 🟠 / Accelerating 🔴]

What's happening: [2 sentences]
Why it matters: [1-2 sentences on real-world impact]
Your opportunity: [1 sentence — how you could benefit or prepare]

━━━━━━━━━━━━━━━━━

📈 *TREND 2: [Name]*
🏷️ Category: [...]
📊 Signal strength: [...]

What's happening: [2 sentences]
Why it matters: [1-2 sentences]
Your opportunity: [1 sentence]

━━━━━━━━━━━━━━━━━

📈 *TREND 3: [Name]*
🏷️ Category: [...]
📊 Signal strength: [...]

What's happening: [2 sentences]
Why it matters: [1-2 sentences]
Your opportunity: [1 sentence]

━━━━━━━━━━━━━━━━━

🔭 *WILD CARD TO WATCH*
[One unusual thing on the fringe that could become big — 2 sentences]

Keep each trend section tight. Total under 350 words."""

    content = ask_claude(prompt, system=system, max_tokens=800)
    send_message(content)
