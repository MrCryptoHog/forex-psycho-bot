# 🧠 ForexMindsetBot

A **premium Telegram bot** for forex trading psychology self-assessment. Built with aiogram 3.x, fully async, production-ready.

Users run `/psychology` to take a randomized 10-question quiz, get scored out of 10, and receive personalized improvement tips based on their tier.

---

## ✨ Features

- **65 unique questions** covering FOMO, revenge trading, discipline, risk management, emotional control, journaling, tilt, greed, patience, and more
- **Every quiz is different** — 10 random questions from the bank, shuffled each time
- **Inline keyboards** — tap to answer, zero typing, buttery smooth flow
- **3-tier scoring** with personalized feedback:
  - 🏆 **8-10**: Elite Mindset — strong praise + polish tips
  - 💪 **5-7**: Solid Foundation — practical action items
  - 💎 **0-4**: Diamond in the Rough — comprehensive level-up plan
- **FSM per-user state** — multiple users can quiz simultaneously
- `/cancel` support at any point
- Clean project structure, type hints, full logging

---

## 🚀 Quick Start (Under 5 Minutes)

### 1. Get a Telegram Bot Token

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the prompts
3. Copy the token (looks like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### 2. Clone & Configure

```bash
git clone <your-repo-url>
cd forex-psycho-bot

# Create your .env file
cp .env.example .env
# Edit .env and paste your bot token
nano .env
```

### 3. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run

```bash
python -m bot.main
```

That's it! Open Telegram, find your bot, and type `/psychology`.

---

## 🐳 Deploy with Docker

```bash
# Build & run
docker build -t forex-mindset-bot .
docker run -d --env-file .env --name forex-bot forex-mindset-bot
```

---

## 🚂 Deploy on Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**
3. Add `BOT_TOKEN` as an environment variable in the Railway dashboard
4. Railway auto-detects the `railway.toml` and deploys — done!

---

## 🌐 Deploy on Render

1. Push to GitHub
2. Go to [render.com](https://render.com) → **New** → **Background Worker**
3. Connect your repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python -m bot.main`
6. Add `BOT_TOKEN` environment variable
7. Deploy!

---

## 🖥️ Deploy on VPS

```bash
# On your server
git clone <your-repo-url>
cd forex-psycho-bot
pip install -r requirements.txt

# Run with systemd, screen, tmux, or nohup:
nohup python -m bot.main &
```

---

## 📁 Project Structure

```
forex-psycho-bot/
├── bot/
│   ├── __init__.py
│   ├── main.py            ← Entry point (polling setup)
│   ├── config.py           ← Environment/config loader
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── common.py       ← /start, /help commands
│   │   └── quiz.py         ← /psychology, answer callbacks, /cancel
│   ├── keyboards/
│   │   ├── __init__.py
│   │   └── quiz_kb.py      ← Inline keyboard builder
│   ├── states/
│   │   ├── __init__.py
│   │   └── quiz.py         ← FSM state definitions
│   ├── data/
│   │   ├── __init__.py
│   │   ├── questions.py     ← 65 question bank + scoring
│   │   └── scoring.py      ← Result tiers + tip generation
│   └── utils/
│       └── __init__.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── Procfile
├── railway.toml
└── README.md
```

---

## ➕ Adding New Questions

Open `bot/data/questions.py` and append a new dict to `QUESTION_BANK`:

```python
{
    "text": "Your question here?",
    "options": [
        "Answer A",
        "Answer B (this is the best-practice one)",
        "Answer C",
        "Answer D",
    ],
    "scores": [0, 1, 0, 0],  # 1 = correct best-practice answer
},
```

Rules:
- Exactly **4 options** per question
- Exactly **4 scores** — one must be `1`, the rest `0`
- The bot auto-validates this on startup (assertion check)
- No restart needed if running with hot-reload; otherwise restart the bot

---

## ⚙️ Swapping to Redis Storage

In `bot/main.py`, replace:

```python
storage = MemoryStorage()
```

with:

```python
from aiogram.fsm.storage.redis import RedisStorage
storage = RedisStorage.from_url("redis://localhost:6379/0")
```

Add `redis` to `requirements.txt` and you're done.

---

## 📄 License

MIT — use it, fork it, make money with it. Trade well. 🧠💰
