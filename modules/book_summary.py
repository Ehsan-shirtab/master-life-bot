from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


BOOK_LIST = [
    # Novels & Classics
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
    ("Don Quixote", "Miguel de Cervantes", "novel"),
    ("Anna Karenina", "Leo Tolstoy", "novel"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", "novel"),
    ("Moby Dick", "Herman Melville", "novel"),
    ("Jane Eyre", "Charlotte Bronte", "novel"),
    ("Wuthering Heights", "Emily Bronte", "novel"),
    ("The Catcher in the Rye", "J.D. Salinger", "novel"),
    # Biographies & Memoirs
    ("The Diary of a Young Girl", "Anne Frank", "biography"),
    ("Long Walk to Freedom", "Nelson Mandela", "biography"),
    ("Leonardo da Vinci", "Walter Isaacson", "biography"),
    ("Steve Jobs", "Walter Isaacson", "biography"),
    ("Educated", "Tara Westover", "memoir"),
    ("The Glass Castle", "Jeannette Walls", "memoir"),
    ("Born a Crime", "Trevor Noah", "memoir"),
    ("I Know Why the Caged Bird Sings", "Maya Angelou", "memoir"),
    # Philosophy & Wisdom
    ("Meditations", "Marcus Aurelius", "philosophy"),
    ("The Art of War", "Sun Tzu", "philosophy"),
    ("Man's Search for Meaning", "Viktor Frankl", "philosophy"),
    # Science & History
    ("A Brief History of Time", "Stephen Hawking", "science"),
    ("Sapiens", "Yuval Noah Harari", "history"),
    ("Cosmos", "Carl Sagan", "science"),
    # Self Development
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

    system = """You are a master storyteller who retells books in a warm, 
immersive, story-like way. You write in clear intermediate English so that 
anyone can enjoy and understand the story deeply.

Your writing rules:
- Write like you are telling a friend the story of a book you love
- Use simple but beautiful sentences
- Describe scenes, characters, emotions, and places vividly
- For novels: tell the complete story from beginning to end, including the ending
- For biographies: tell the person's full life as a human story
- For philosophy: explain ideas through stories and real life examples
- For science and history: tell it as a fascinating human journey of discovery
- Never use bullet points
- Never use asterisks, underscores, dashes as decoration, or any markdown
- Write in flowing paragraphs only
- Write at least 1500 words so the reader feels they truly read the whole book
- The tone should feel like sitting by a fireplace listening to a great storyteller"""

    prompt = f"""Tonight's book is: {book_title} by {book_author}
Genre: {book_category}

Write a complete, long, story-like retelling of this entire book in intermediate 
English. The reader should feel like they are actually reading the book itself, 
not a school summary.

Follow this structure:

Start by setting the scene. Where does this story take place? What is the world 
of this book? Who are the main characters? Introduce everything naturally, the 
way a story begins.

Then tell the complete story or content of the book from beginning to end. 
Include all important scenes, characters, turning points, conflicts, and emotions. 
Do not skip the middle or the ending. Every important moment should be described 
with enough detail that the reader can picture it clearly and feel it emotionally.

Write each scene as a paragraph or series of paragraphs. Move through the story 
naturally, the way a good novel flows. Use transitions like "A few days later", 
"That same evening", "As weeks passed", "On the morning of" to guide the reader 
through time.

End with a final section that begins with the words: What this book leaves you with.
In this section, reflect on the deepest message or feeling of the book. What does 
it say about life, people, love, courage, money, power, or time? Write this as a 
warm, thoughtful paragraph that stays with the reader as they fall asleep.

Write at least 1500 words. Use clear intermediate English throughout.
Plain text only. No special characters or formatting symbols."""

    content = ask_claude(prompt, system=system, max_tokens=2048)

    message = (
        f"Bedtime Reading - {date_str}\n\n"
        f"Tonight: {book_title}\n"
        f"By: {book_author}\n"
        f"Genre: {book_category.title()}\n\n"
        f"{'─' * 30}\n\n"
        f"{content}\n\n"
        f"{'─' * 30}\n\n"
        f"Sleep well. A new book waits tomorrow night."
    )

    send_message(message)
