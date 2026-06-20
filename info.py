import os
from dotenv import load_dotenv

load_dotenv()

# ── Bot ────────────────────────────────────────────────────────────────────────
BOT_TOKEN: str = os.environ["BOT_TOKEN"]
BOT_USERNAME: str = os.environ.get("BOT_USERNAME", "")

# ── MongoDB ────────────────────────────────────────────────────────────────────
MONGO_URI: str = os.environ["MONGO_URI"]
MONGO_DB_NAME: str = os.environ.get("MONGO_DB_NAME", "Cluster0")

# ── Server (keep-alive) ────────────────────────────────────────────────────────
PORT: int = int(os.environ.get("PORT", 8080))
PING_URL: str = os.environ.get("RENDER_EXTERNAL_URL", f"")

# ── Bot behaviour ──────────────────────────────────────────────────────────────
PING_INTERVAL_MINUTES: int = int(os.environ.get("PING_INTERVAL_MINUTES", 10))
