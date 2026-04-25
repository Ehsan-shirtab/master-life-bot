from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


BOOK_LIST = [
    # Novels & Stories
    ("The Alchemist", "Paulo Coelho", "novel"),
    ("The Old Man and the Sea", "Ernest Hemingway", "novel"),
    ("Animal Farm", "George Orwell", "novel"),
    ("The Great Gatsby", "F. Scott Fitzgerald", "novel"),
    ("Of Mice and Men", "John Steinbeck", "novel"),
    ("The Little Prince", "Antoine de Saint-Exupery", "novel"),
    ("Siddhartha", "Hermann Hesse", "novel"),
    ("The Stranger", "Albert Camus", "novel"),
    ("Brave New World", "Aldous Huxley", "novel"),
    ("1984", "George Orwell", "novel"),
    # Biographies & True Stories
    ("The Diary of a Young Girl", "Anne Frank", "biography"),
    ("Long Walk to Freedom", "Nelson Mandela", "biography"),
    ("Leonardo da Vinci", "Walter Isaacson", "biography"),
    ("Elon Musk", "Walter Isaacson", "biography"),
    ("Steve Jobs", "Walter Isaacson", "biography"),
    ("Educated", "Tara Westover", "memoir"),
    ("The Glass Castle", "Jeannette Walls", "memoir"),
    ("Born a Crime", "Trevor Noah", "memoir"),
    # Philosophy & Wisdom
    ("Meditations", "Marcus Aurelius", "philosophy"),
    ("The Art of War", "Sun Tzu", "philosophy"),
    ("Man's Search for Meaning", "Viktor Frankl", "philosophy"),
    ("The Republic", "Plato", "philosophy"),
    ("Thus Spoke Zarathustra", "Friedrich Nietzsche", "philosophy"),
    # Science & Discovery
    ("A Brief History of Time", "Stephen Hawking", "science"),
    ("Sapiens", "Yuval Noah Harari", "science"),
    ("The Selfish Gene", "Richard Dawkins", "science"),
    ("Cosmos", "Carl Sagan", "science"),
    ("The Origin of Species", "Charles Darwin", "science"),
    # Self Development
    ("Atomic Habits", "James Clear", "self-development"),
    ("Thinking Fast and Slow", "Daniel Kahneman", "self-development"),
    ("The Psychology of Money", "Morgan Housel", "self-development"),
    ("Deep Work", "Cal Newport", "self-development"),
    ("Man's Search for Meaning", "Viktor Frankl", "self-development"),
]


def get_tonights_book():
    day_num = date.today().toordinal()
    return BOOK_LIST[day_num % len(BOOK_LIST)]


def send_book_summary():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")

    book_title, book_author, book_category = get_tonights_book()

    system = """You are a master storyteller who brings books completely to life.
Your job is to give someone the FULL experience of reading an entire book in one 
sitting — every important scene, idea, character, and lesson.

Your writing style:
- Rich, immersive, flowing prose — never dry or academic
- For novels: tell the full story with vivid scenes, characters, emotions, and plot
- For biographies: bring the person to life with their struggles, triumphs, and lessons
- For philosophy: make ancient or complex ideas feel alive and personally relevant
- For science: tell the story of the discovery and why it changes how we see the world
- Write as if you are the most engaging professor who ever lived
- The reader should feel they truly experienced the whole book
- No bullet points. No markdown. Pure flowing prose only.
- Write at least 1500 words — this is a full bedtime reading experience"""

    prompt = f"""Tonight's book is: {book_title} by {book_author}
Genre: {book_category}
Date: {date_str}

Write a complete, immersive, full-book experience. Cover the ENTIRE book tonight.

Start with a compelling opening that sets the mood and tells the reader why this 
book matters and why it has stood the test of time.

Then take the reader through the COMPLETE journey of the book:

For novels and memoirs: Tell the full story from beginning to end. Introduce every 
major character vividly. Describe the key scenes with emotion and detail. Do not 
skip the ending. Make the reader feel every turning point.

For philosophy and self-development: Walk through every major idea in the book from 
start to finish. Use real examples and stories to make each concept come alive. 
Connect every idea to real modern life.

For science and history: Tell the full story of the discovery or events. Explain 
every major concept clearly and beautifully. Share the human stories behind the 
science or history.

For biographies: Tell the person's full life story. Their childhood, struggles, 
breakthroughs, failures, greatest moments, and lasting legacy.

End with a section called WHAT THIS BOOK LEAVES YOU WITH — the deepest lesson or 
feeling the book gives you, and why it stays with you long after the last page.

Write at least 1500 words. This is a complete book experience, not a summary.
Plain text only. No asterisks, no underscores, no special characters."""

    content = ask_claude(prompt, system=system, max_tokens=2048)

    message = (
        f"Bedtime Reading - {date_str}\n\n"
        f"Tonight's Book: {book_title}\n"
        f"Author: {book_author}\n"
        f"Genre: {book_category.title()}\n\n"
        f"{'─' * 30}\n\n"
        f"{content}\n\n"
        f"{'─' * 30}\n"
        f"Sleep well. A new book waits tomorrow night."
    )

    send_message(message)
