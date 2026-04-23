"""
modules/analytics.py
Module 7: Sunday Life Dashboard
Sent every Sunday at 8:00 AM Vancouver time.

What it does:
- Weekly recap of everything the bot delivered that week
- Highlights the most important ideas from each module
- Gives you a "weekly intelligence briefing" — what you learned
- Motivates you for the coming week
- Since no external storage is used, it generates a smart weekly summary
  based on what the week's content would have covered
"""

from utils.claude import ask_claude
from utils.telegram import send_message
from datetime import datetime, date, timedelta


def send_analytics():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    week_num = today.isocalendar()[1]

    # Calculate week range
    week_start = today - timedelta(days=today.weekday() + 1)
    week_end = today
    week_range = f"{week_start.strftime('%b %d')} – {week_end.strftime('%b %d, %Y')}"

    # Get what book was covered this week
    from modules.book_summary import get_this_weeks_book, BOOK_LIST
    from modules.skill_of_week import get_week_skill

    book_title, book_author, _ = get_this_weeks_book()
    skill = get_week_skill()

    # Get next week's book and skill
    next_week_book = BOOK_LIST[(week_num + 1) % len(BOOK_LIST)]
    next_skill_categories = [
        "communication & persuasion", "productivity & time management",
        "Excel & spreadsheet shortcuts", "Python & coding basics",
        "financial literacy", "negotiation & influence",
        "critical thinking & logic", "clear professional writing",
        "speed reading & comprehension", "memory techniques & mnemonics",
        "public speaking & confidence", "problem solving frameworks",
    ]
    next_skill = next_skill_categories[(week_num + 1) % len(next_skill_categories)]

    system = """You are a personal life intelligence assistant creating a Sunday 
weekly review. Be encouraging, insightful, and forward-looking. 
Write like a smart friend reviewing your week with you."""

    prompt = f"""Create a Sunday Weekly Life Dashboard for week {week_num} of the year.
Date: {date_str}
Week covered: {week_range}

This week the user received:
- Daily AI/Tech breakthroughs (Mon-Sun)
- Skill of the Week: {skill}
- Daily Second Brain captures (rotating topics: psychology, future of work, health, economics, philosophy, nature, history)
- Weekly Trend Radar (Monday)
- Daily Bedtime Book: "{book_title}" by {book_author}
- Daily English Immersion (rotating: idioms, phrasal verbs, vocabulary, writing tips, pronunciation, Canadian English, business English)

Next week:
- Book: "{next_week_book[0]}" by {next_week_book[1]}
- Skill: {next_skill}

Format EXACTLY:

☀️ *SUNDAY LIFE DASHBOARD*
_Week {week_num} · {week_range}_

━━━━━━━━━━━━━━━

🧠 *THIS WEEK YOU LEARNED*

📡 Tech & AI: [1 sentence summarizing the kind of breakthroughs covered this week]
💡 Skill: Progressed through *{skill}* — Mon intro, Wed practice, Fri real-world example
📚 Book: Explored "{book_title}" — [1 sentence on the book's core theme]
🌍 Second Brain: [Topics like psychology, economics, philosophy — 1 sentence]
📈 Trend Radar: [1 sentence on the type of trends spotted this week]
🇨🇦 English: 7 lessons across idioms, vocabulary, writing & Canadian expressions

━━━━━━━━━━━━━━━

💭 *REFLECTION PROMPTS*
1. [A thought-provoking question about growth this week]
2. [A question connecting this week's learning to real life]

━━━━━━━━━━━━━━━

🔭 *NEXT WEEK PREVIEW*
📚 Book: *{next_week_book[0]}* by {next_week_book[1]}
💡 Skill: {next_skill}
📡 Tech briefings continue daily at 7 AM
🌙 Bedtime reading every night at 9 PM

━━━━━━━━━━━━━━━

🌱 *WEEKLY INTENTION*
[One powerful sentence to set a positive intention for the coming week]

_You showed up this week. That's everything. 💪_

Keep it motivating and under 300 words."""

    content = ask_claude(prompt, system=system, max_tokens=700)
    send_message(content)
