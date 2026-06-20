import logging

from pyrogram import Client
from pyrogram.storage import MemoryStorage

import info
from db.database import init_db
from keep_alive import keep_alive

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

app = Client(
    name="tgbot",
    api_id=info.API_ID,
    api_hash=info.API_HASH,
    bot_token=info.BOT_TOKEN,
    storage=MemoryStorage("tgbot"),   # no disk writes — safe on ephemeral hosts
    plugins=dict(root="plugins"),
)

if __name__ == "__main__":
    init_db()
    keep_alive()
    print("Bot is running...")
    app.run()
