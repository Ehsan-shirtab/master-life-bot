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
    ("Daring Greatly", "Brene Brown", "vulnerability & courage"),
    ("Start With Why", "Simon Sinek", "purpose & leadership"),
    ("The Alchemist", "Paulo Coelho", "purpose & following your path"),
    ("Flow", "Mihaly Csikszentmihalyi", "optimal experience & engagement"),
    ("Quiet", "Susan Cain", "introversion & harnessing your strengths"),
]

DAY_THEMES = [
    "the opening of the story, the world the author builds, and the central question the book asks",
    "the most surprising and counterintuitive idea in this book that challenges common thinking",
    "the deepest practical wisdom in this book and how it changes the way you live day to day",
    "the most powerful story or scene in the book and why it stays with you long after reading",
    "how the core ideas of this book connect to real modern life, relationships, and daily decisions",
    "the most memorable and meaningful quotes from the book and the deep truth behind each one",
    "the complete journey of the book, its lasting message, and why every person should experience it",
]


def get_this_weeks_book():
    week_num = date.today().isocalendar()[1]
    return BOOK_LIST[week_num % len(BOOK_LIST)]


def send_book_summary():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    day_of_week = today.weekday()
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = day_names[day_of_week]

    book_title, book_author, book_category = get_this_weeks_book()
    day_theme = DAY_THEMES[day_of_week]
    tomorrow_theme = DAY_THEMES[(day_of_week + 1) % 7]

    system = """You are a master storyteller and literary companion who brings books 
to life at bedtime. You write in a warm, deep, immersive voice — like a wise and 
brilliant friend who has read thousands of books and loves sharing them.

Your writing style:
- Rich, flowing, unhurried prose that feels like being told a story
- You paint pictures with words — the reader feels transported
- You weave between the book's world and real human emotions seamlessly  
- You treat the reader as intelligent and curious
- Your tone is intimate, like a late night conversation by a fireplace
- You never summarize like a book report — you illuminate like a poet
- You make the reader FEEL the book, not just understand it
- No bullet points ever. No markdown symbols. Pure flowing prose only.
- Write at least 800 words — this should take 8 to 10 minutes to read slowly"""

    prompt = f"""Tonight you are sharing: {book_title} by {book_author}
Category: {book_category}
Tonight is Day {day_of_week + 1} of 7. Tonight's deep focus: {day_theme}

Write a rich, immersive, beautifully crafted bedtime reading experience.

Begin with a warm, poetic opening paragraph that sets the mood and draws the reader 
into the world of this book. Make them feel they are settling in for something special.

Then spend the heart of the piece going deeply into: {day_theme}
This is not a summary. This is an experience. Write as if you are slowly walking 
the reader through the most meaningful rooms of this book, pausing in each one, 
letting them feel the weight and beauty of the ideas. Use scenes from the book. 
Use the author's own ideas but expressed in your warm storytelling voice. 
Connect the book's world to the reader's inner life — their hopes, fears, 
relationships, choices, and dreams.

Then write a closing section called "Before You Sleep" — a gentle, reflective 
passage that leaves the reader with one profound thought to carry into their dreams. 
Not a question. A thought. Something that lingers like the last note of a song.

End with one sentence: "Tomorrow night we explore: {tomorrow_theme}"

Write at least 800 words. This is bedtime literature, not a summary.
Plain text only. No asterisks, no underscores, no special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)

    message = (
        f"Bedtime Reading - {date_str}\n\n"
        f"Book: {book_title}\n"
        f"Author: {book_author}\n"
        f"Night {day_of_week + 1} of 7\n\n"
        f"{'─' * 30}\n\n"
        f"{content}\n\n"
        f"{'─' * 30}\n"
        f"Sleep well. The book continues tomorrow."
    )

    send_message(message)
