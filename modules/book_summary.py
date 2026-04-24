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
    day_of_week = today.weekday()
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = day_names[day_of_week]

    book_title, book_author, book_category = get_this_weeks_book()
    day_theme = DAY_THEMES[day_of_week]
    tomorrow_theme = DAY_THEMES[(day_of_week + 1) % 7]

    system = """You are a bedtime reading companion. Your summaries are calm, 
thoughtful, and easy to absorb before sleep. You help people learn the key 
ideas of great books without needing to read every page. Write in a warm, 
conversational tone. Never overwhelming, always calming and insightful.
Never use asterisks, underscores, or any markdown symbols in your response."""

    prompt = f"""Tonight's book is: {book_title} by {book_author}
Category: {book_category}
Today is {day_name}. Tonight's focus: {day_theme}

Write exactly three sections:

TONIGHTS FOCUS:
Write 3 to 4 calm paragraphs about {day_theme} from this book.
Be specific, reference actual content from the book.
No bullet points, flowing prose only.

SLEEP ON THIS:
One gentle question or reflection to think about before sleeping.

TOMORROW:
One sentence previewing tomorrow's focus: {tomorrow_theme}

Total response must be under 300 words. Plain text only, no special characters."""

    # --- NEW GEMINI 2.5 ENGINE ---
    client = genai.Client()
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': system}
        )
        content = response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        content = f"⚠️ System Error: Could not generate summary. ({e})"
    # -----------------------------

    message = (
        f"🌙 Bedtime Reading — {date_str}\n\n"
        f"📚 {book_title}\nby {book_author}\n"
        f"Day {day_of_week + 1} of 7\n\n"
        f"{'─' * 25}\n\n"
        f"{content}\n\n"
        f"{'─' * 25}\n"
        f"Sleep well."
    )

    send_message(message)
