from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError

import info

# Shared client — reused by both MongoStorage (session) and db models
client: MongoClient | None = None


def get_client() -> MongoClient:
    global client
    if client is None:
        if not info.MONGO_URI or info.MONGO_URI.startswith("mongodb+srv://<"):
            raise RuntimeError(
                "MONGO_URI is not set or still has the placeholder value. "
                "Set it in your Render dashboard → Environment."
            )
        client = MongoClient(info.MONGO_URI, serverSelectionTimeoutMS=10000)
    return client


def get_db() -> Database:
    return get_client()[info.MONGO_DB_NAME]


def init_db():
    try:
        db = get_db()
        db.command("ping")
        db["users"].create_index("user_id", unique=True)
        print(f"[db] Connected to MongoDB — database: {info.MONGO_DB_NAME}")
    except RuntimeError:
        raise
    except (ServerSelectionTimeoutError, ConfigurationError) as e:
        raise RuntimeError(
            f"Could not connect to MongoDB. Check MONGO_URI.\nDetail: {e}"
        ) from e
    except Exception as e:
        raise RuntimeError(f"Unexpected DB error: {e}") from e
