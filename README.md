# 🤖 Master Life Bot
### Powered by Google Gemini (100% Free)

One bot. 7 modules. Runs automatically every day.
Uses **Google Gemini 1.5 Flash** — completely free, no credit card needed.

---

## 📅 Daily Schedule (Vancouver / BC Time)

| Time | Module | Frequency |
|------|--------|-----------|
| 7:00 AM | 🔬 AI & Tech Breakthrough | Every day |
| 8:00 AM | 📈 Trend Radar | Every Monday |
| 9:00 AM | 💡 Skill of the Week | Mon / Wed / Fri |
| 12:00 PM | 🇨🇦 English Immersion | Every day |
| 9:00 PM | 📚 Bedtime Book Summary | Every night |
| 9:30 PM | 🧠 Second Brain Auto-Capture | Every night |
| 8:00 AM | ☀️ Life Dashboard | Every Sunday |

**Bonus:** Message the bot any URL or topic → instant Second Brain summary.

---

## 🗂️ Project Structure

```
master-life-bot/
├── main.py
├── modules/
│   ├── tech_news.py
│   ├── skill_of_week.py
│   ├── second_brain.py
│   ├── trend_radar.py
│   ├── book_summary.py
│   ├── language.py
│   └── analytics.py
├── utils/
│   ├── telegram.py
│   └── ai.py                ← Google Gemini (FREE)
├── requirements.txt
├── .env.example
├── render.yaml
└── README.md
```

---

## 🚀 Step-by-Step Setup

### Step 1 — Get FREE Google Gemini API Key

1. Go to: **https://aistudio.google.com/app/apikey**
2. Sign in with Google account
3. Click **"Create API Key"**
4. Copy the key (starts with `AIzaSy...`)

> Free limits: 1,500 requests/day — plenty for all 7 modules.

---

### Step 2 — Create Telegram Bot

1. Open Telegram → search **@BotFather**
2. Send `/newbot` → follow steps → copy the **bot token**
3. Send any message to your new bot (e.g. "hi")
4. Get your Chat ID by visiting:
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```
5. Find `"chat":{"id": 123456789}` — that's your **Chat ID**

---

### Step 3 — Push to GitHub

```bash
cd master-life-bot
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/master-life-bot.git
git push -u origin main
```

---

### Step 4 — Deploy on Render

1. Go to **https://render.com** → New → Web Service
2. Connect GitHub → select `master-life-bot`
3. Add these **Environment Variables**:

   | Key | Value |
   |-----|-------|
   | `TELEGRAM_TOKEN` | Your bot token |
   | `TELEGRAM_CHAT_ID` | Your chat ID |
   | `GEMINI_API_KEY` | Your Gemini API key |
   | `BOT_SECRET` | Any random string |

4. Deploy → wait ~2 minutes

---

### Step 5 — Register Telegram Webhook

Paste this in your browser (replace values):
```
https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://master-life-bot.onrender.com/webhook
```
You should see: `{"ok": true}`

✅ **Done! Bot is live.**

---

## 🧪 Test Any Module

```
https://master-life-bot.onrender.com/run?module=tech_news&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=skill&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=trend_radar&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=book_summary&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=language&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=analytics&secret=YOUR_SECRET
```

---

## ⏰ UTC Time Reference (Vancouver)

| Module | Vancouver | UTC Summer | UTC Winter |
|--------|-----------|------------|------------|
| Tech News | 7:00 AM | 14:00 | 15:00 |
| Trend Radar | Mon 8:00 AM | Mon 15:00 | Mon 16:00 |
| Skill | 9:00 AM | 16:00 | 17:00 |
| English | 12:00 PM | 19:00 | 20:00 |
| Book / Second Brain | 9–9:30 PM | 04:00–04:30 +1d | 05:00–05:30 +1d |
| Dashboard | Sun 8:00 AM | Sun 15:00 | Sun 16:00 |

> Update `render.yaml` schedules in November and March when clocks change.

---

## 🆓 Total Cost: $0

| Service | Cost |
|---------|------|
| Google Gemini API | Free |
| Telegram Bot API | Free |
| Render | Free tier |
| GitHub | Free |
