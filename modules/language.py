"""
modules/language.py
Module 6: English Language Immersion
Sent every day at 12:00 PM Vancouver time.

What it does:
- Teaches advanced/nuanced English — beyond basics
- Focuses on: idioms, phrasal verbs, business English, pronunciation tips,
  writing style, vocabulary in context, Canadian expressions
- Each day has a different focus area
- Always practical — real sentences you can use immediately
"""

from utils.ai import ask_claude
from utils.telegram import send_message
from datetime import datetime, date


# Rotate daily focus areas
DAILY_FOCUS = [
    ("idiom", "an English idiom commonly used in Canada/North America"),
    ("phrasal_verb", "a useful phrasal verb used in professional settings"),
    ("vocabulary", "an advanced vocabulary word that sounds intelligent in conversation"),
    ("writing_tip", "a writing tip to make emails and messages clearer and more professional"),
    ("pronunciation", "a commonly mispronounced English word or tricky sound"),
    ("canadian_english", "a Canadian English expression, slang, or cultural reference"),
    ("business_english", "a business English phrase used in meetings, emails, or negotiations"),
]


def send_language_lesson():
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    day_index = date.today().toordinal() % len(DAILY_FOCUS)
    focus_key, focus_desc = DAILY_FOCUS[day_index]

    system = """You are an English language teacher for an intermediate-advanced 
learner living in Victoria, British Columbia, Canada. Your lessons are practical, 
clear, and immediately useful. You give real examples from everyday Canadian life. 
You're encouraging and never condescending. Focus on nuance, not basics."""

    if focus_key == "idiom":
        prompt = f"""Teach one English idiom today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Idiom_

💬 *IDIOM: "[the idiom]"*

📖 *MEANING*
[Clear explanation of what it means]

🗣️ *HOW TO USE IT*
[When/where is it appropriate to use this?]

✅ *EXAMPLE SENTENCES*
1. "[Natural sentence using it]"
2. "[Another example in a different context]"

❌ *COMMON MISTAKE*
[How people sometimes misuse or misunderstand this idiom]

🇨🇦 *CANADIAN CONTEXT*
[Is this used in Canada? Any regional notes?]

🧠 *MEMORY TIP*
[One trick to remember this idiom]"""

    elif focus_key == "phrasal_verb":
        prompt = f"""Teach one phrasal verb today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Phrasal Verb_

⚡ *PHRASAL VERB: "[verb + particle]"*

📖 *MEANING*
[What does it mean? Does it have multiple meanings?]

✅ *EXAMPLE SENTENCES*
1. "[Example in casual conversation]"
2. "[Example in professional/work setting]"
3. "[Example in writing]"

🔄 *SIMILAR EXPRESSIONS*
[1-2 alternatives with the same meaning]

💼 *PROFESSIONAL USE*
[Is this appropriate in formal/work English? Notes on register.]"""

    elif focus_key == "vocabulary":
        prompt = f"""Teach one advanced vocabulary word today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Advanced Vocabulary_

📝 *WORD: "[word]"*
_Part of speech: [noun/verb/adjective/adverb]_
_Pronunciation: /[phonetic spelling]/_

📖 *MEANING*
[Clear, simple definition]

✅ *EXAMPLE SENTENCES*
1. "[Sentence showing the word in context]"
2. "[Another sentence — different context]"

🔗 *WORD FAMILY*
[Related forms: e.g. noun → verb → adjective]

💡 *WHEN TO USE THIS*
[Formal writing? Casual speech? Professional emails?]

🧠 *MEMORY TIP*
[Etymology or memory trick]"""

    elif focus_key == "writing_tip":
        prompt = f"""Give one practical English writing tip today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Writing Tip_

✍️ *TIP: "[Short name for the tip]"*

📖 *THE RULE*
[Explain the writing principle clearly]

❌ *WEAK WRITING*
"[Example of writing WITHOUT this tip]"

✅ *STRONG WRITING*
"[Same content WITH this tip applied]"

📧 *IN EMAILS*
[How to apply this specifically to emails or messages]

🎯 *PRACTICE*
[A quick writing exercise to practice this today]"""

    elif focus_key == "pronunciation":
        prompt = f"""Teach correct pronunciation of a tricky English word today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Pronunciation_

🗣️ *WORD: "[word]"*

❌ *COMMON MISPRONUNCIATION*
How most people say it wrong: /[wrong phonetic]/
[Why people make this mistake]

✅ *CORRECT PRONUNCIATION*
How to say it: /[correct phonetic]/
Sounds like: "[describe using familiar sounds]"

🔤 *SYLLABLE BREAKDOWN*
[Break it into syllables: "SYL-la-ble"]

💡 *MEMORY TIP*
[Trick to remember the correct pronunciation]

📍 *EXAMPLE IN SENTENCE*
"[A natural sentence using the word correctly]" """

    elif focus_key == "canadian_english":
        prompt = f"""Teach a Canadian English expression or cultural language note today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Canadian English_

🍁 *EXPRESSION: "[Canadian expression or word]"*

📖 *MEANING*
[What does it mean?]

🌍 *CANADIAN vs OTHERS*
[How do Americans or British say the same thing differently?]

✅ *USE IT IN A SENTENCE*
"[Natural example]"

😄 *FUN FACT*
[Something interesting about this word or Canadian English in general]

📍 *WHERE YOU'LL HEAR IT*
[Victoria BC context — where/when would you encounter this?]"""

    else:  # business_english
        prompt = f"""Teach one business English phrase today. Date: {date_str}

Format EXACTLY:

🇨🇦 *English Immersion — {date_str}*
📌 _Today's Focus: Business English_

💼 *PHRASE: "[business phrase]"*

📖 *MEANING IN BUSINESS CONTEXT*
[What does it mean in professional settings?]

✅ *HOW TO USE IT*
In a meeting: "[Example]"
In an email: "[Example]"
In a report: "[Example]"

⚠️ *COMMON MISTAKE*
[How non-native speakers sometimes misuse this]

🔄 *FORMAL vs INFORMAL VERSION*
Formal: "[phrase]"
Casual: "[equivalent casual version]" """

    content = ask_claude(prompt, system=system, max_tokens=600)
    send_message(content)
