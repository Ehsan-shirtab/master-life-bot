"""
modules/book_summary.py
Module 5: Bedtime Book Summary
Sent every night at 9:00 PM Vancouver time.

What it does:
- Each week covers ONE book (same book Mon-Sun, different chapter/concept daily)
- Books rotate weekly across categories: psychology, productivity, finance,
  philosophy, science, leadership, habits, communication
- Perfect for reading before bed: calm, educational, 2-minute read
- By end of week you've absorbed the whole book's key ideas
"""

from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


BOOK_LIST = [
    ("Atomic Habits", "James Clear", "habits & self-improvement"),
    ("Thinking, Fast and Slow", "Daniel Kahneman", "psychology & decision making"),
    ("The Psychology of Money", "Morgan Housel", "personal finance & mindset"),
    ("Deep Work", "Cal Newport", "productivity & focus"),
    ("Sapiens", "Yuval Noah Harari", "history & human civilization"),
    ("Man's Search for Meaning", "Viktor Frankl", "philosophy & resilience"),
    ("The 7 Habits of Highly Effective People", "Stephen Covey", "leadership & personal development"),
    ("Meditations", "Marcus Aurelius", "stoic philosophy"),
    ("The Lean Startup", "Eric Ries", "entrepreneurship & innovation"),
    ("How to Win Friends and Influence People", "Dale Carnegie", "communication & relationships"),
    ("The Power of Now", "Eckhart Tolle", "mindfulness & presence"),
    ("Outliers", "Malcolm Gladwell", "success & what drives it"),
    ("The Subtle Art of Not Giving a F*ck", "Mark Manson", "values & priorities"),
    ("Essentialism", "Greg McKeown", "focus & eliminating the non-essential"),
    ("The 4-Hour Workweek", "Tim Ferriss", "lifestyle design & efficiency"),
    ("Daring Greatly", "Brené Brown", "vulnerability & courage"),
    ("Start With Why", "Simon Sinek", "purpose & leadership"),
    ("The Alchemist", "Paulo Coelho", "purpose & following your path"),
    ("Flow", "Mihaly Csikszentmihalyi", "optimal experience & engagement"),
    ("Quiet", "Susan Cain", "introversion & harnessing your strengths"),
]

DAY_THEMES = [
    "the core problem this book solves and the author's main argument",
    "the most surprising or counterintuitive idea in this book",
    "the most practical, actionable advice from this book",
    "a story or case study from this book that illustrates the key concept",
    "how the ideas in this book apply to modern daily life",
    "the most memorable quote and its deeper meaning",
    "the overall summary, key takeaways, and whether to read the full book",
]


def get_this_weeks_book():
    week_num = date.today().isocalendar()[1]
    return BOOK_LIST[week_num % len(BOOK_LIST)]


def send_book_summary():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    day_of_week = today.weekday()  # 0=Mon ... 6=Sun

    book_title, book_author, book_category = get_this_weeks_book()
    day_theme = DAY_THEMES[day_of_week]

    # Day label
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = day_names[day_of_week]

    system = """You are a bedtime reading companion. Your summaries are calm, 
thoughtful, and easy to absorb before sleep. You help people learn the key 
ideas of great books without needing to read every page. Write in a warm, 
conversational tone. Never overwhelming — always calming and insightful."""

    prompt = f"""Tonight's book is: "{book_title}" by {book_author}
Category: {book_category}
Today ({day_name}) focus: {day_theme}

Write a bedtime summary in this EXACT format:

🌙 *Bedtime Reading — {date_str}*

📚 *{book_title}*
_by {book_author} · Day {day_of_week + 1} of 7_

━━━━━━━━━━━━━━━

✨ *TONIGHT'S FOCUS*
_{day_theme.capitalize()}_

[Write 3-4 calm, well-crafted paragraphs covering tonight's theme from this book. 
Be specific — reference actual content from the book. 
Write as if you're a wise friend sharing something interesting before bed.
No bullet points — flowing prose only tonight.]

━━━━━━━━━━━━━━━

💭 *SLEEP ON THIS*
[One gentle question or thought to reflect on as you fall asleep]

😴 _Sleep well. Tomorrow: {DAY_THEMES[(day_of_week + 1) % 7]}_

Keep it under 280 words. Calm and thoughtful."""

    content = ask_claude(prompt, system=system, max_tokens=700)
    send_message(content)
