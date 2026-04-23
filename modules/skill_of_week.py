"""
modules/skill_of_week.py
Module 2: Skill of the Week — sent Mon / Wed / Fri at 9:00 AM

What it does:
- Monday:    Introduces the week's micro-skill with full explanation
- Wednesday: Gives a practical exercise to apply it
- Friday:    Gives a real-world example + recap + next steps

Skills rotate across categories:
communication, productivity, tech, finance, negotiation, 
critical thinking, writing, speed reading, memory techniques
"""

import os
from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date
import hashlib


SKILL_CATEGORIES = [
    "communication & persuasion",
    "productivity & time management",
    "Excel & spreadsheet shortcuts",
    "Python & coding basics",
    "financial literacy",
    "negotiation & influence",
    "critical thinking & logic",
    "clear professional writing",
    "speed reading & comprehension",
    "memory techniques & mnemonics",
    "public speaking & confidence",
    "problem solving frameworks",
]


def get_week_skill():
    """Deterministically pick this week's skill category based on week number."""
    week_num = date.today().isocalendar()[1]
    return SKILL_CATEGORIES[week_num % len(SKILL_CATEGORIES)]


def send_skill():
    today = datetime.now()
    weekday = today.weekday()  # 0=Mon, 2=Wed, 4=Fri
    skill = get_week_skill()
    date_str = today.strftime("%B %d, %Y")

    if weekday == 0:  # Monday
        day_label = "📖 *INTRODUCTION*"
        instruction = f"""It's Monday — introduce this week's micro-skill on {skill}.

Format EXACTLY:
🎯 *SKILL OF THE WEEK*
[Skill name — make it specific, not just the category]

📖 *WHAT IS IT?*
[2-3 sentences explaining the skill clearly]

🤔 *WHY LEARN THIS?*
[1-2 sentences: real benefit in daily life or career]

⚡ *CORE CONCEPT*
[The single most important idea to understand about this skill]

📅 *THIS WEEK'S PLAN*
Mon: Learn the concept (today!)
Wed: Practice exercise
Fri: Real-world example + recap"""

    elif weekday == 2:  # Wednesday
        day_label = "💪 *PRACTICE DAY*"
        instruction = f"""It's Wednesday — give a hands-on practice exercise for this week's skill: {skill}.

Format EXACTLY:
💪 *PRACTICE EXERCISE — {skill.upper()}*

🎯 *TODAY'S CHALLENGE*
[One specific, doable 10-minute exercise to practice this skill]

📝 *STEP BY STEP*
1. [Step 1]
2. [Step 2]  
3. [Step 3]

✅ *SUCCESS LOOKS LIKE*
[How they know they did it right]

⏱️ *Time needed: 10-15 minutes*"""

    else:  # Friday
        day_label = "🏆 *REAL WORLD EXAMPLE*"
        instruction = f"""It's Friday — give a real-world example and weekly recap for this week's skill: {skill}.

Format EXACTLY:
🏆 *REAL-WORLD EXAMPLE — {skill.upper()}*

🌍 *HOW A PRO USES THIS*
[A specific, realistic example of someone using this skill effectively]

💬 *BEFORE vs AFTER*
Before: [Without this skill]
After: [With this skill]

🔑 *KEY TAKEAWAY*
[The one thing to remember from this whole week]

📚 *GO DEEPER*
[One book, YouTube channel, or resource to master this skill]"""

    system = "You are a concise, practical skills coach. Be specific, actionable, and encouraging. No fluff."
    content = ask_claude(instruction, system=system, max_tokens=500)

    message = f"💡 *Skill of the Week — {date_str}*\n\n{content}"
    send_message(message)
