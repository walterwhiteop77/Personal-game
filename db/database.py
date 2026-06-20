from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError

import info

_client: MongoClient | None = None


def get_db() -> Database:
    global _client
    if _client is None:
        if not info.MONGO_URI or info.MONGO_URI.startswith("mongodb+srv://<"):
            raise RuntimeError(
                "MONGO_URI is not set or still has the placeholder value. "
                "Set it in your Render dashboard → Environment."
            )
        _client = MongoClient(info.MONGO_URI, serverSelectionTimeoutMS=10000)
    return _client[info.MONGO_DB_NAME]


def init_db():
    try:
        db = get_db()
        db.command("ping")                              # verify connection is live
        db["users"].create_index("user_id", unique=True)
        print(f"[db] Connected to MongoDB — database: {info.MONGO_DB_NAME}")
    except (ServerSelectionTimeoutError, ConfigurationError) as e:
        raise RuntimeError(
            f"Could not connect to MongoDB. Check your MONGO_URI env var.\nDetail: {e}"
        ) from e
