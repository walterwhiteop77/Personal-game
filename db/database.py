from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError

import info

_client: MongoClient | None = None


def get_db() -> Database:
    global _client
    if _client is None:
        _client = MongoClient(info.MONGO_URI, serverSelectionTimeoutMS=10000)
    return _client[info.MONGO_DB_NAME]


def init_db() -> None:
    try:
        db = get_db()
        db.command("ping")
        db["users"].create_index("user_id", unique=True)
        print(f"[db] MongoDB connected — db: {info.MONGO_DB_NAME}")
    except (ServerSelectionTimeoutError, ConfigurationError) as e:
        raise RuntimeError(f"MongoDB connection failed. Check MONGO_URI.\n{e}") from e
