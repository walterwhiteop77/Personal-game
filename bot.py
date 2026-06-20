import logging
import importlib
from pathlib import Path

from telegram import Update
from telegram.ext import ApplicationBuilder

import info
from db.database import init_db
from keep_alive import keep_alive

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def load_plugins(app):
    plugins_dir = Path(__file__).parent / "plugins"
    for file in sorted(plugins_dir.glob("*.py")):
        if file.name.startswith("_"):
            continue
        module = importlib.import_module(f"plugins.{file.stem}")
        if hasattr(module, "register"):
            module.register(app)
            logger.info(f"Loaded plugin: {file.stem}")


def main():
    init_db()
    keep_alive()

    app = ApplicationBuilder().token(info.BOT_TOKEN).build()
    load_plugins(app)

    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
