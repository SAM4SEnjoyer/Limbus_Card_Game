
import random
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN
#AJOUTER ET GERER LE NOMBRE DE CARTES DANS LA MAIN


def draw(Hand, DeckName, Number_of_cards, cursor, connection):
    sql = f"SELECT Deck_ID FROM decks WHERE Name=%s AND Type=%s"
    cursor.execute(sql, (DeckName, 'in_game'))
    deck_id = cursor.fetchone()
    for i in range(Number_of_cards):
        sql = f"SELECT * FROM card_in_deck WHERE Deck_ID=%s"
        cursor.execute(sql, deck_id['Deck_ID'])
        Deck_List = cursor.fetchall()
        print(Deck_List)
        card = random.choice(Deck_List)
        sql = f"INSERT INTO cards_in_hand (Card_ID, Hand_ID) VALUES (%s,%s)"
        cursor.execute(sql, (card['Card_ID'], Hand))
        sql = f"DELETE FROM card_in_deck WHERE card_in_deck_ID=%s"
        cursor.execute(sql, card['card_in_deck_ID'])
        sql = f"SELECT Number_of_Cards FROM decks WHERE Deck_ID=%s"
        cursor.execute(sql, deck_id['Deck_ID'])
        num= cursor.fetchone()["Number_of_Cards"]-1
        sql = f"UPDATE decks SET Number_of_Cards=%s WHERE Deck_ID=%s"
        cursor.execute(sql, (num, deck_id['Deck_ID']))
    connection.commit()
    return True

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
