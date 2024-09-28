
import random

def init(cursor, connection, session):
    sql=f"INSERT INTO hand (User_ID) VALUES (%s)"
    cursor.execute(sql, (session['Account_ID']))
    connection.commit()
    sql=f"SELECT LAST_INSERT_ID()"
    cursor.execute(sql)
    session['Hand_Used_ID'] = cursor.fetchone()["LAST_INSERT_ID()"]
    session['Number_in_Hand'] = 0
    draw(session['Hand_Used_ID'], session['Deck_Used_ID'], 5, cursor, connection, session)


def draw(Hand, Deck_ID, Number_of_cards, cursor, connection, session):
    for i in range(Number_of_cards):
        sql = f"SELECT * FROM card_in_deck WHERE Deck_ID=%s"
        cursor.execute(sql, Deck_ID)
        Deck_List = cursor.fetchall()
        print(Deck_List)
        card = random.choice(Deck_List)
        sql = f"INSERT INTO cards_in_hand (Card_ID, Hand_ID) VALUES (%s,%s)"
        cursor.execute(sql, (card['Card_ID'], Hand))
        sql = f"DELETE FROM card_in_deck WHERE card_in_deck_ID=%s"
        cursor.execute(sql, card['card_in_deck_ID'])
        sql = f"SELECT Number_of_Cards FROM decks WHERE Deck_ID=%s"
        cursor.execute(sql, Deck_ID)
        num= cursor.fetchone()["Number_of_Cards"]-1
        sql = f"UPDATE decks SET Number_of_Cards=%s WHERE Deck_ID=%s"
        cursor.execute(sql, (num, Deck_ID))
        session['Number_in_Hand'] += 1
    connection.commit()
    return True

def discard(Card_ID, cursor, connection):
    sql = f"DELETE FROM cards_in_hand WHERE card_in_hand_ID=%s"
    cursor.execute(sql, Card_ID)
    connection.commit()

def fullClear(cursor, connection):
    sql = f"SELECT Deck_ID FROM decks WHERE Type=%s OR Type=%s"
    cursor.execute(sql, ('in_game', 'discard'))
    deck_id = cursor.fetchall()
    for deck in deck_id:
        sql = f"DELETE FROM card_in_deck WHERE Deck_ID=%s"
        cursor.execute(sql, deck['Deck_ID'])
    sql = f"DELETE FROM decks WHERE Type=%s"
    cursor.execute(sql,"in_game")
    cursor.execute(sql,"discard")
    tables = ["cards_in_hand", "cards_in_board", "decks_in_board", "hand", "user_in_game"]
    for table in tables:
        sql = f"DELETE FROM {table}"
        cursor.execute(sql)
    connection.commit()
