from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong!")


def register(app):
    app.add_handler(CommandHandler("ping", ping))
