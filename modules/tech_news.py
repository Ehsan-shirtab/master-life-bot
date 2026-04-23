"""
modules/tech_news.py
Module 1: AI & Tech Breakthrough of the Day
Sent every morning at 7:00 AM Vancouver time.

What it does:
- Uses Claude + web search awareness to generate today's most important
  AI/tech/science breakthrough
- Explains it in plain English: what happened + what it means for your life
"""

from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime


def send_tech_news():
    today = datetime.now().strftime("%B %d, %Y")

    system = """You are a tech intelligence briefing bot for a curious non-expert.
Your job is to identify ONE real, significant breakthrough or development 
happening right now in AI, science, or technology — and explain it in a way 
that a smart non-technical person can understand in under 2 minutes.

Format your response EXACTLY like this (use these exact emoji headers):

🔬 *TODAY'S BREAKTHROUGH*
[One sentence: what happened]

🌍 *WHY IT MATTERS*
[2-3 sentences: real-world impact on regular people]

💡 *WHAT YOU SHOULD KNOW*
[1-2 sentences: the bigger picture or trend this fits into]

🔗 *LEARN MORE*
[Suggest ONE search term or website to learn more about this topic]

Keep the total response under 200 words. Be specific — never vague or generic.
Today's date: """ + today

    prompt = f"""Give me today's most important and fascinating breakthrough or development 
in AI, technology, or science as of {today}. Focus on something that happened 
recently (within the last week ideally). Make it genuinely interesting and 
relevant to daily life."""

    content = ask_claude(prompt, system=system, max_tokens=500)

    message = f"🌅 *Good Morning — Tech Briefing*\n_{today}_\n\n{content}"
    send_message(message)
