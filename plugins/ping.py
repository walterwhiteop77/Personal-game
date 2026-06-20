from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("ping"))
async def ping(_: Client, message: Message):
    if not message.from_user:
        return
    await message.reply_text("Pong! 🏓")
