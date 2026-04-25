from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date, timedelta


def send_analytics():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    week_num = today.isocalendar()[1]

    week_start = today - timedelta(days=today.weekday() + 1)
    week_end = today
    week_range = f"{week_start.strftime('%b %d')} - {week_end.strftime('%b %d, %Y')}"

    from modules.skill_of_week import get_week_skill, SKILL_CATEGORIES
    skill = get_week_skill()
    next_skill = SKILL_CATEGORIES[(week_num + 1) % len(SKILL_CATEGORIES)]

    system = """You are a personal life intelligence assistant creating a Sunday
weekly review. Be encouraging, insightful, and forward-looking.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""Create a Sunday Weekly Life Dashboard for week {week_num}.
Date: {date_str}
Week covered: {week_range}
This week skill focus: {skill}
Next week skill: {next_skill}

Format exactly like this:

SUNDAY LIFE DASHBOARD
Week {week_num} - {week_range}

THIS WEEK YOU LEARNED:
Tech and AI: One sentence on breakthroughs covered this week.
Skill: This week focused on {skill}.
Books: A different classic book every night.
Second Brain: Ideas from psychology, economics, philosophy, science, and history.
Trend Radar: Three growing trends spotted this week.
English: Seven daily lessons across idioms, vocabulary, writing, and expressions.

REFLECTION PROMPTS:
1. One thought provoking question about this week's growth.
2. One question connecting learning to a real life decision.

NEXT WEEK PREVIEW:
Skill: {next_skill}
Books: New classics every night.
Everything else continues on schedule.

WEEKLY INTENTION:
One warm powerful sentence to carry into next week.

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
