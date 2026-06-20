from datetime import datetime, timezone
from .database import get_db


def upsert_user(user_id: int, username: str | None, first_name: str | None) -> None:
    get_db()["users"].update_one(
        {"user_id": user_id},
        {
            "$set": {
                "username":   username,
                "first_name": first_name,
                "last_seen":  datetime.now(timezone.utc),
            },
            "$setOnInsert": {
                "user_id":   user_id,
                "joined_at": datetime.now(timezone.utc),
            },
        },
        upsert=True,
    )


def get_user(user_id: int) -> dict | None:
    return get_db()["users"].find_one({"user_id": user_id}, {"_id": 0})


def count_users() -> int:
    return get_db()["users"].count_documents({})


def get_all_user_ids() -> list[int]:
    return [d["user_id"] for d in get_db()["users"].find({}, {"user_id": 1})]
