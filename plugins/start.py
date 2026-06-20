from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from db.models import upsert_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    upsert_user(user.id, user.username, user.first_name)
    await update.message.reply_text(
        f"Hello {user.first_name}! I'm alive and ready."
    )


def register(app):
    app.add_handler(CommandHandler("start", start))
