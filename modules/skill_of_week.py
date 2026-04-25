from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


SKILL_CATEGORIES = [
    "communication and persuasion",
    "productivity and time management",
    "Excel and spreadsheet shortcuts",
    "Python and coding basics",
    "financial literacy",
    "negotiation and influence",
    "critical thinking and logic",
    "clear professional writing",
    "speed reading and comprehension",
    "memory techniques and mnemonics",
    "public speaking and confidence",
    "problem solving frameworks",
]


def get_week_skill():
    week_num = date.today().isocalendar()[1]
    return SKILL_CATEGORIES[week_num % len(SKILL_CATEGORIES)]


def send_skill():
    today = datetime.now()
    weekday = today.weekday()
    skill = get_week_skill()
    date_str = today.strftime("%B %d, %Y")

    if weekday == 0:
        instruction = f"""It is Monday. Introduce this week's micro-skill: {skill}.
Date: {date_str}

Write in this format:

SKILL OF THE WEEK - {date_str}

SKILL: [Specific skill name]

WHAT IS IT:
Two to three sentences explaining the skill clearly.

WHY LEARN THIS:
One to two sentences on the real benefit in daily life or career.

CORE CONCEPT:
The single most important idea to understand about this skill.

THIS WEEK'S PLAN:
Monday: Learn the concept (today)
Wednesday: Practice exercise
Friday: Real world example and recap

Plain text only. No special characters."""

    elif weekday == 2:
        instruction = f"""It is Wednesday. Give a hands-on practice exercise for: {skill}.
Date: {date_str}

Write in this format:

SKILL PRACTICE - {date_str}
This week: {skill}

TODAY'S CHALLENGE:
One specific doable 10 minute exercise to practice this skill.

STEP BY STEP:
Step 1: [what to do]
Step 2: [what to do]
Step 3: [what to do]

SUCCESS LOOKS LIKE:
How you know you did it right.

Time needed: 10 to 15 minutes.

Plain text only. No special characters."""

    else:
        instruction = f"""It is Friday. Give a real world example and recap for: {skill}.
Date: {date_str}

Write in this format:

SKILL RECAP - {date_str}
This week: {skill}

HOW A PRO USES THIS:
A specific realistic example of someone using this skill effectively.

BEFORE AND AFTER:
Before learning this skill: [description]
After learning this skill: [description]

KEY TAKEAWAY:
The one thing to remember from this whole week.

GO DEEPER:
One book, YouTube channel, or free resource to master this skill.

Plain text only. No special characters."""

    system = """You are a concise practical skills coach.
Be specific, actionable, and encouraging. No fluff.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    content = ask_claude(instruction, system=system, max_tokens=1000)
    send_message(content)
