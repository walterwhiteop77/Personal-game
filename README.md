# Telegram Bot (Pyrogram + MongoDB)

A plugin-based Telegram bot built with Pyrogram v2 and MongoDB.

## Structure

```
tgbot/
├── bot.py              ← Entry point
├── info.py             ← All config variables (reads from .env)
├── keep_alive.py       ← HTTP server + self-ping for free hosting
├── requirements.txt
├── .env.example
│
├── plugins/            ← Drop any .py file here to add commands
│   ├── start.py        ← /start
│   ├── help.py         ← /help
│   └── ping.py         ← /ping
│
└── db/
    ├── database.py     ← MongoDB connection + init
    └── models.py       ← upsert_user, get_user, count_users
```

## Setup

### 1. Get your credentials

| Variable   | Where to get it |
|------------|-----------------|
| `API_ID`   | https://my.telegram.org → App credentials |
| `API_HASH` | https://my.telegram.org → App credentials |
| `BOT_TOKEN`| [@BotFather](https://t.me/BotFather) → /newbot |
| `MONGO_URI`| [MongoDB Atlas](https://cloud.mongodb.com) → Connect → Drivers |

### 2. Install & run

```bash
git clone <your-repo>
cd tgbot

python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# Fill in your values in .env

python bot.py
```

## Adding a plugin

Create a new file in `plugins/`. No registration needed — Pyrogram picks it up automatically:

```python
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("hello"))
async def hello(client: Client, message: Message):
    await message.reply_text("Hello!")
```

## Deploy (Render / Koyeb / Railway)

Set these env vars in the dashboard:

```
API_ID, API_HASH, BOT_TOKEN, MONGO_URI
```

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `python bot.py`
