import logging

from pyrogram import Client
from pyrogram.storage.mongo_storage import MongoStorage

import info
from db.database import get_client, init_db
from keep_alive import keep_alive

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# MongoStorage takes (name, mongo_client_instance, database_name)
app = Client(
    name="tgbot",
    api_id=info.API_ID,
    api_hash=info.API_HASH,
    bot_token=info.BOT_TOKEN,
    storage=MongoStorage("tgbot", get_client(), info.MONGO_DB_NAME),
    plugins=dict(root="plugins"),
)

if __name__ == "__main__":
    init_db()
    keep_alive()
    print("Bot is running...")
    app.run()
