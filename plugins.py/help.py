from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


HELP_TEXT = """
Available commands:
/start  — Register and say hello
/help   — Show this message
/ping   — Check if bot is alive
"""


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


def register(app):
    app.add_handler(CommandHandler("help", help_cmd))
