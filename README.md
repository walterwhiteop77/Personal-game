# Telegram Bot

A simple plugin-based Telegram bot using python-telegram-bot v21 with SQLite storage.

## Structure

```
tgbot/
├── bot.py              ← Entry point, loads plugins automatically
├── requirements.txt
├── .env.example
│
├── plugins/            ← Drop any .py file here to add commands
│   ├── start.py        ← /start command
│   ├── help.py         ← /help command
│   └── ping.py         ← /ping command
│
└── db/                 ← Database layer
    ├── database.py     ← SQLite connection + init
    └── models.py       ← Query helpers (upsert_user, get_user, etc.)
```

## Adding a plugin

Create a new file in `plugins/`, implement your handler, then add a `register(app)` function:

```python
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

def register(app):
    app.add_handler(CommandHandler("hello", hello))
```

That's it — `bot.py` picks it up automatically on next start.

## Setup

```bash
# 1. Clone and enter the repo
git clone <your-repo>
cd tgbot

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your token
cp .env.example .env
# Edit .env and set BOT_TOKEN=your_token_here

# 5. Run
python bot.py
```

## Deploy (Koyeb / Render / Railway)

Set the `BOT_TOKEN` environment variable in the dashboard and use:

- **Start command:** `python bot.py`
- **Build command:** `pip install -r requirements.txt`
