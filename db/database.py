from pymongo import MongoClient
from pymongo.database import Database

import info

_client: MongoClient | None = None


def get_db() -> Database:
    global _client
    if _client is None:
        _client = MongoClient(info.MONGO_URI)
    return _client[info.MONGO_DB_NAME]


def init_db():
    db = get_db()
    db["users"].create_index("user_id", unique=True)
    print(f"[db] Connected to MongoDB — database: {info.MONGO_DB_NAME}")
