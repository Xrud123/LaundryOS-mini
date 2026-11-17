from database import init_database, DB_PATH
import sqlite3

def card_reader():
    card_uid = "CC"
    return card_uid

def get_balance(card_uid):
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM cards
        WHERE card_uid = ?
        """, (card_uid,))
        result = cursor.fetchone()
        if result is not None:
            print(f"Card UID: {result[0]}")
            print(f"Balance: {result[1]}")
        else:
            print("Card was not found")
    except sqlite3.OperationalError as error:
        print(f"Database operation error: {error}")
    finally:
        if connection is not None:
            connection.close()

def add_credits(card_uid):
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        with connection:
            cursor.execute("""
            UPDATE cards
            SET balance = balance + 2
            WHERE card_uid = ?
            """, (card_uid,))
        if cursor.rowcount == 1:
            print("Balance changed successfully")
        else:
            print("Balance was not changed or card was not found")
    except sqlite3.OperationalError as error:
        print(f"Database operation error: {error}")
    finally:
        if connection is not None:
            connection.close()

def reset_card(card_uid):
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        with connection:
            cursor.execute("""
            UPDATE cards
            SET balance = 0
            WHERE card_uid = ?
            """, (card_uid,))
        if cursor.rowcount == 1:
            print("Card balance reset successfully")
        else:
            print("Card balance was not cleaned")
    except sqlite3.OperationalError as error:
        print(f"Database operation error: {error}")
    finally:
        if connection is not None:
            connection.close()


def main():
    print("Starting LaundryOS...")
    init_database()
    get_balance(card_reader())
    add_credits(card_reader())
    get_balance(card_reader())
    reset_card(card_reader())
    get_balance(card_reader())



if __name__ == "__main__":
    main()
