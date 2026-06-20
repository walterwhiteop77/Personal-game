import os
from dotenv import load_dotenv

load_dotenv()

# ── Telegram API ── https://my.telegram.org ────────────────────────────────────
API_ID: int    = int(os.environ["API_ID"])
API_HASH: str  = os.environ["API_HASH"]

# ── Bot token ── @BotFather ────────────────────────────────────────────────────
BOT_TOKEN: str    = os.environ["BOT_TOKEN"]
BOT_USERNAME: str = os.environ.get("BOT_USERNAME", "")

# ── MongoDB ────────────────────────────────────────────────────────────────────
MONGO_URI: str     = os.environ["MONGO_URI"]
MONGO_DB_NAME: str = os.environ.get("MONGO_DB_NAME", "tgbot")

# ── Keep-alive ─────────────────────────────────────────────────────────────────
PORT: int                  = int(os.environ.get("PORT", 8080))
PING_INTERVAL_MINUTES: int = int(os.environ.get("PING_INTERVAL_MINUTES", 14))

# ── Optional ───────────────────────────────────────────────────────────────────
_owner = os.environ.get("OWNER_ID", "0")
OWNER_ID: int = int(_owner) if _owner.isdigit() else 0
