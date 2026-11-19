from database import init_database, DB_PATH
import sqlite3

def card_reader():
    card_uid = "AA"
    return card_uid

def get_balance(card_uid):
    connection = None
    result = None
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM cards
        WHERE card_uid = ?
        """, (card_uid,))
        result = cursor.fetchone()
    finally:
        if connection is not None:
            connection.close()
    return result

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
        return cursor.rowcount == 1
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
        return cursor.rowcount == 1
    finally:
        if connection is not None:
            connection.close()


def main():
    print("Starting LaundryOS...")
    try:
        card_uid = card_reader()
        init_database()
        card_data = get_balance(card_uid)
        if card_data is not None:
            print(f"Card ID: {card_data[0]}; Balance: {card_data[1]}")
        else:
            print("Card was not found")
        success = add_credits(card_uid)
        if success:
            print("Balance updated successfully")
        else:
            print("Card was not found")
        reset = reset_card(card_uid)
        if reset:
            print("Card balance reset successfully")
        else:
            print("Card was not found")
    except sqlite3.OperationalError as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    main()
