import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from db.models import upsert_user


@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    user = message.from_user
    if not user:
        return
    # run blocking pymongo call in a thread so the event loop is not blocked
    await asyncio.to_thread(upsert_user, user.id, user.username, user.first_name)
    await message.reply_text(
        f"Hello {user.first_name}! I'm alive and ready."
    )
