import os
from dotenv import load_dotenv

load_dotenv()

# ── Telegram API (from https://my.telegram.org) ────────────────────────────────
API_ID: int = int(os.environ["API_ID"])
API_HASH: str = os.environ["API_HASH"]

# ── Bot (from @BotFather) ──────────────────────────────────────────────────────
BOT_TOKEN: str = os.environ["BOT_TOKEN"]
BOT_USERNAME: str = os.environ.get("BOT_USERNAME", "")

# ── MongoDB ────────────────────────────────────────────────────────────────────
MONGO_URI: str = os.environ["MONGO_URI"]
MONGO_DB_NAME: str = os.environ.get("MONGO_DB_NAME", "tgbot")

# ── Server (keep-alive) ────────────────────────────────────────────────────────
PORT: int = int(os.environ.get("PORT", 8080))
PING_URL: str = os.environ.get("RENDER_EXTERNAL_URL", f"http://localhost:{PORT}")
PING_INTERVAL_MINUTES: int = int(os.environ.get("PING_INTERVAL_MINUTES", 14))

# ── Bot settings ───────────────────────────────────────────────────────────────
OWNER_ID: int = int(os.environ.get("OWNER_ID", 0))
