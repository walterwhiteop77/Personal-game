from .database import get_connection


def upsert_user(user_id: int, username: str | None, first_name: str | None):
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO users (id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                username   = excluded.username,
                first_name = excluded.first_name
            """,
            (user_id, username, first_name),
        )


def get_user(user_id: int):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else None


def count_users() -> int:
    with get_connection() as conn:
        row = conn.execute("SELECT COUNT(*) as n FROM users").fetchone()
        return row["n"]
