import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "data" / "laundry.db"


def init_database(db_path=DB_PATH):
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_path)
    try:
        with connection:
            connection.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                card_uid TEXT NOT NULL UNIQUE,
                balance INTEGER NOT NULL DEFAULT 0
                    CHECK (balance >= 0)
            )
            """)
    finally:
        connection.close()

    print("Database initialized successfully!")
