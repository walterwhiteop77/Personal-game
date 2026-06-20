from pyrogram import Client, filters
from pyrogram.types import Message

HELP_TEXT = """
**Available commands:**
/start — Register and say hello
/help  — Show this message
/ping  — Check if bot is alive
"""


@Client.on_message(filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply_text(HELP_TEXT)
