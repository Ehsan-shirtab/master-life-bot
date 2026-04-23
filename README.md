# 🤖 Master Life Bot

One bot. 7 modules. Runs automatically every day to keep you informed, educated, and growing.

---

## 📅 Daily Schedule

| Time (Vancouver) | Module | Frequency |
|-----------------|--------|-----------|
| 7:00 AM | 🔬 AI & Tech Breakthrough | Every day |
| 8:00 AM | 📈 Trend Radar | Every Monday |
| 9:00 AM | 💡 Skill of the Week | Mon / Wed / Fri |
| 12:00 PM | 🇨🇦 English Immersion | Every day |
| 9:00 PM | 📚 Bedtime Book Summary | Every night |
| 9:30 PM | 🧠 Second Brain Auto-Capture | Every night |
| 8:00 AM Sunday | ☀️ Life Dashboard | Every Sunday |

**Bonus:** Message the bot any time with a URL or topic → it summarizes it for your Second Brain instantly.

---

## 🗂️ Project Structure

```
master-life-bot/
├── main.py                  ← Flask app, all routes
├── modules/
│   ├── tech_news.py         ← AI & Tech Breakthrough
│   ├── skill_of_week.py     ← Skill of the Week (Mon/Wed/Fri)
│   ├── second_brain.py      ← Second Brain (auto + user-triggered)
│   ├── trend_radar.py       ← Weekly Trend Radar
│   ├── book_summary.py      ← Bedtime Book Summary
│   ├── language.py          ← English Immersion
│   └── analytics.py         ← Sunday Life Dashboard
├── utils/
│   ├── telegram.py          ← Send Telegram messages
│   └── claude.py            ← Claude API wrapper
├── requirements.txt
├── .env.example             ← Copy to .env and fill in
├── render.yaml              ← Full Render deployment config
└── README.md
```

---

## 🚀 Setup & Deployment

### Step 1 — Create a Telegram Bot

1. Open Telegram, search for **@BotFather**
2. Send `/newbot` and follow the steps
3. Copy your **bot token** (looks like `123456:ABC-DEF...`)
4. Send any message to your new bot
5. Get your chat ID: visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
6. Find `"chat":{"id":XXXXXXX}` — that number is your **chat ID**

### Step 2 — Get Your API Keys

- **Anthropic API Key:** https://console.anthropic.com → API Keys → Create Key
- **Bot Secret:** Run `openssl rand -hex 16` in terminal (any random string)

### Step 3 — Push to GitHub

```bash
cd master-life-bot
git init
git add .
git commit -m "Initial commit — Master Life Bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/master-life-bot.git
git push -u origin main
```

### Step 4 — Deploy on Render

1. Go to https://render.com → New → **Web Service**
2. Connect your GitHub repo
3. Render detects `render.yaml` automatically
4. Add your environment variables in Render dashboard:
   - `TELEGRAM_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `ANTHROPIC_API_KEY`
   - `BOT_SECRET`
5. Click **Deploy**
6. Wait ~2 minutes for the first deploy to finish

### Step 5 — Register Telegram Webhook

After deploy, run this URL in your browser (replace values):

```
https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://master-life-bot.onrender.com/webhook
```

You should see: `{"ok":true,"result":true}`

Now when you send a message to your bot on Telegram, it will process it through the Second Brain module!

---

## 🧪 Test Each Module

Test any module manually by visiting these URLs in your browser:

```
https://master-life-bot.onrender.com/run?module=tech_news&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=skill&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=trend_radar&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=book_summary&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=language&secret=YOUR_SECRET
https://master-life-bot.onrender.com/run?module=analytics&secret=YOUR_SECRET
```

---

## 📖 How the Second Brain Works

**Auto mode (daily 9:30 PM):** The bot automatically captures one fascinating idea each night.

**Manual mode (anytime):** Send a message directly to your Telegram bot:
- Send a URL → Bot summarizes the article with key ideas
- Send a topic (e.g. "quantum computing") → Bot researches and captures key knowledge
- Bot stores everything in formatted Telegram messages you can search later

---

## ⏰ UTC Time Reference (Vancouver)

| Vancouver Time | UTC (Summer PDT) | UTC (Winter PST) |
|---------------|-----------------|-----------------|
| 7:00 AM | 14:00 | 15:00 |
| 8:00 AM | 15:00 | 16:00 |
| 9:00 AM | 16:00 | 17:00 |
| 12:00 PM | 19:00 | 20:00 |
| 9:00 PM | 04:00 (+1 day) | 05:00 (+1 day) |
| 9:30 PM | 04:30 (+1 day) | 05:30 (+1 day) |

Update `render.yaml` cron schedules when clocks change in November and March.

---

## 💡 Customization Tips

- **Change book list:** Edit `BOOK_LIST` in `modules/book_summary.py`
- **Change skill topics:** Edit `SKILL_CATEGORIES` in `modules/skill_of_week.py`
- **Change language focus:** Edit `DAILY_FOCUS` in `modules/language.py`
- **Add a new module:** Create `modules/new_module.py` with a `send_new_module()` function, then add it to `MODULES` dict in `main.py` and add a cron job in `render.yaml`

---

## 🛠️ Built With

- **Python + Flask** — Web server
- **Claude API (Anthropic)** — All AI content generation
- **Telegram Bot API** — Message delivery
- **Render** — Hosting + Cron jobs
- **GitHub** — Version control
