from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


BOOK_LIST = [
    ("The Great Gatsby", "F. Scott Fitzgerald", "novel"),
    ("The Alchemist", "Paulo Coelho", "novel"),
    ("The Old Man and the Sea", "Ernest Hemingway", "novel"),
    ("Animal Farm", "George Orwell", "novel"),
    ("Of Mice and Men", "John Steinbeck", "novel"),
    ("The Little Prince", "Antoine de Saint-Exupery", "novel"),
    ("Siddhartha", "Hermann Hesse", "novel"),
    ("The Stranger", "Albert Camus", "novel"),
    ("Brave New World", "Aldous Huxley", "novel"),
    ("1984", "George Orwell", "novel"),
    ("Crime and Punishment", "Fyodor Dostoevsky", "novel"),
    ("The Count of Monte Cristo", "Alexandre Dumas", "novel"),
    ("Les Miserables", "Victor Hugo", "novel"),
    ("Anna Karenina", "Leo Tolstoy", "novel"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", "novel"),
    ("Jane Eyre", "Charlotte Bronte", "novel"),
    ("Wuthering Heights", "Emily Bronte", "novel"),
    ("The Catcher in the Rye", "J.D. Salinger", "novel"),
    ("The Diary of a Young Girl", "Anne Frank", "biography"),
    ("Long Walk to Freedom", "Nelson Mandela", "biography"),
    ("Leonardo da Vinci", "Walter Isaacson", "biography"),
    ("Steve Jobs", "Walter Isaacson", "biography"),
    ("Educated", "Tara Westover", "memoir"),
    ("The Glass Castle", "Jeannette Walls", "memoir"),
    ("Born a Crime", "Trevor Noah", "memoir"),
    ("I Know Why the Caged Bird Sings", "Maya Angelou", "memoir"),
    ("Meditations", "Marcus Aurelius", "philosophy"),
    ("The Art of War", "Sun Tzu", "philosophy"),
    ("Man's Search for Meaning", "Viktor Frankl", "philosophy"),
    ("A Brief History of Time", "Stephen Hawking", "science"),
    ("Sapiens", "Yuval Noah Harari", "history"),
    ("Cosmos", "Carl Sagan", "science"),
    ("Atomic Habits", "James Clear", "self-development"),
    ("Thinking Fast and Slow", "Daniel Kahneman", "self-development"),
    ("The Psychology of Money", "Morgan Housel", "self-development"),
]


def get_tonights_book():
    day_num = date.today().toordinal()
    return BOOK_LIST[day_num % len(BOOK_LIST)]


def send_book_summary():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    book_title, book_author, book_category = get_tonights_book()

    system = """You are a master storyteller who retells books in warm flowing
prose in intermediate English. You write like you are telling a beloved story
to a friend before bed. Never use asterisks, underscores, or any markdown.
Plain text only. Write complete stories with a clear beginning, middle, and end."""

    prompt = f"""Tonight's book: {book_title} by {book_author}
Genre: {book_category}

Write a COMPLETE story-like retelling of this entire book from start to finish.
The reader must get the whole story in one reading tonight, not continued tomorrow.

Rules:
- Write in flowing paragraphs, intermediate English
- Include all major characters, scenes, turning points, and the ending
- Write exactly like the example below in style and length
- Minimum 1200 words, maximum 1600 words
- End with a section starting with: What this book leaves you with
- Plain text only, no special characters

Style example: 
The story takes place in the summer of 1922 in Long Island near New York City. 
It is told by a young man named Nick Carraway. Nick comes from the Midwest and 
moves east to work in the bond business. He rents a small house in a wealthy area 
called West Egg. Right next door stands a huge beautiful mansion owned by a 
mysterious man named Jay Gatsby...

Now write the complete story of {book_title} in this same style."""

    content = ask_claude(prompt, system=system, max_tokens=2048)

    header = (
        f"Bedtime Reading - {date_str}\n"
        f"Tonight: {book_title}\n"
        f"By: {book_author}\n"
        f"{'─' * 30}\n\n"
    )

    footer = f"\n\n{'─' * 30}\nSleep well. A new book waits tomorrow night."

    full_message = header + content + footer
    send_message(full_message)
