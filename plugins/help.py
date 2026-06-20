from pyrogram import Client, filters
from pyrogram.types import Message

HELP_TEXT = """
**Commands:**
/start — Register and say hello
/help  — Show this message
/ping  — Check if bot is alive
"""


@Client.on_message(filters.command("help"))
async def help_cmd(_: Client, message: Message):
    if not message.from_user:
        return
    await message.reply_text(HELP_TEXT)
