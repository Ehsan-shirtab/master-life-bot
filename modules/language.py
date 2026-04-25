from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


DAILY_FOCUS = [
    ("idiom", "an English idiom commonly used in Canada"),
    ("phrasal_verb", "a useful phrasal verb used in professional settings"),
    ("vocabulary", "an advanced vocabulary word for intelligent conversation"),
    ("writing_tip", "a writing tip to make emails and messages more professional"),
    ("pronunciation", "a commonly mispronounced English word"),
    ("canadian_english", "a Canadian English expression or cultural reference"),
    ("business_english", "a business English phrase for meetings or emails"),
]


def send_language_lesson():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    day_index = date.today().toordinal() % len(DAILY_FOCUS)
    focus_key, focus_desc = DAILY_FOCUS[day_index]

    system = """You are an English language teacher for an intermediate learner
living in Victoria, British Columbia, Canada. Your lessons are practical, clear,
and immediately useful with real examples from everyday Canadian life.
Never use asterisks, underscores, or markdown symbols. Plain text only."""

    prompt = f"""Teach {focus_desc} today. Date: {date_str}

Write in this format:

English Immersion - {date_str}
Today's Focus: {focus_key.replace('_', ' ').title()}

THE LESSON:
[The idiom, word, phrase, or tip being taught today]

MEANING:
[Clear explanation of what it means and when to use it]

EXAMPLE SENTENCES:
1. [Natural sentence using it in everyday life]
2. [Another example in a different context]
3. [One example in a professional or work setting]

COMMON MISTAKE:
[How people sometimes misuse or misunderstand this]

CANADIAN CONTEXT:
[How this is used in Canada, specifically in BC if relevant]

MEMORY TIP:
[One simple trick to remember this]

Plain text only. No special characters."""

    content = ask_claude(prompt, system=system, max_tokens=1000)
    send_message(content)
