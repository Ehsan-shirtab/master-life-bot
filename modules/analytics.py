from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date, timedelta


def send_analytics():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    week_num = today.isocalendar()[1]

    week_start = today - timedelta(days=today.weekday() + 1)
    week_range = f"{week_start.strftime('%b %d')} - {week_end.strftime('%b %d, %Y')}"

    from modules.skill_of_week import get_week_skill
    skill = get_week_skill()

    from modules.skill_of_week import SKILL_CATEGORIES
    next_skill = SKILL_CATEGORIES[(week_num + 1) % len(SKILL_CATEGORIES)]

    system = """You are a personal life intelligence assistant creating a Sunday 
weekly review. Be encouraging, insightful, and forward-looking.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""Create a Sunday Weekly Life Dashboard for week {week_num}.
Date: {date_str}
Week covered: {week_range}
This week's skill focus: {skill}

This week the user received daily AI and tech briefings, skill lessons on {skill}, 
daily English immersion lessons, nightly book summaries of classic literature, 
nightly Second Brain captures, and weekly trend radar.

Format exactly like this:

SUNDAY LIFE DASHBOARD
Week {week_num} - {week_range}

THIS WEEK YOU LEARNED:

Tech and AI: One sentence summarizing the kinds of breakthroughs covered this week.
Skill Focus: Progress through {skill} with Monday introduction, Wednesday practice, Friday real world example.
Books: A different classic book every night this week.
Second Brain: Fascinating ideas from psychology, economics, philosophy, science, and history.
Trend Radar: Three growing trends spotted this week.
English: Seven daily lessons across idioms, vocabulary, writing, pronunciation, and Canadian expressions.

REFLECTION PROMPTS:
1. One thought provoking question about growth this week.
2. One question connecting this week's learning to real life decisions.

NEXT WEEK PREVIEW:
Skill next week: {next_skill}
Books: A new classic every night.
All daily messages continue on their regular schedule.

WEEKLY INTENTION:
One powerful, warm sentence to set a positive intention for the coming week.

Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)

    message = (
        f"Sunday Life Dashboard\n"
        f"Week {week_num} - {date_str}\n\n"
        f"{'─' * 30}\n\n"
        f"{content}\n\n"
        f"{'─' * 30}\n"
        f"Great week. Keep going."
    )

    send_message(message)
