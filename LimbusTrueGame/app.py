from flask import Flask, render_template, session, request
import pymysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ndio3290fn0r043ç%)=BNde'

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='limbuscardproject',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = connection.cursor()

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/Deck_Creation', methods=['GET', 'POST'])
def Deck_Creation():
    Card_Ego_Gift_Info = []
    Card_Sinner_Info = []
    Card_Spell_Info = []
    Card_EGO_Info = []
    Deck_Info = []

    sql = f"SELECT * FROM cards"
    cursor.execute(sql)
    cards_info = cursor.fetchall()

    if not session['Deck_In_Use']:

        sql = f"SELECT * FROM decks"
        cursor.execute(sql)
        Deck_ID = (cursor.fetchone())['Deck_ID']
        session['Deck_In_Use'] = Deck_ID

    if 'deck_id_select' in request.form:
        session['Deck_In_Use'] = request.form['deck_id_select']
        print(session['Deck_In_Use'])

    if 'card_id_add' in request.form:
        card_id = request.form['card_id_add']
        print(card_id)
        sql = f"INSERT INTO card_in_deck (Card_ID, Deck_ID) VALUES (%s, %s)"
        cursor.execute(sql, (card_id, session['Deck_In_Use']))
        connection.commit()

    if 'card_id_remove' in request.form:
        card_id = request.form['card_id_remove']
        print(card_id)
        sql = "SELECT card_in_deck_ID FROM card_in_deck WHERE Deck_ID = %s AND Card_ID = %s"
        cursor.execute(sql, (session['Deck_In_Use'], card_id))
        card_in_deck = cursor.fetchone()
        sql = f"DELETE FROM card_in_deck WHERE card_in_deck_ID = %s"
        cursor.execute(sql, (card_in_deck['card_in_deck_ID'],))
        connection.commit()

    for card in cards_info:
        match card['Card_Type'] :

            case "Sinner" :
                sql = f"SELECT * FROM sinners"
                cursor.execute(sql)
                Card_Sinner_Info = cursor.fetchall()

            case "EGO_Gift" :
                sql = f"SELECT * FROM ego_gifts"
                cursor.execute(sql)
                Card_Ego_Gift_Info = cursor.fetchall()

            case "EGO" :
                sql = f"SELECT * FROM ego"
                cursor.execute(sql)
                Card_EGO_Info = cursor.fetchall()

            case "Spell" :
                sql = f"SELECT * FROM spell"
                cursor.execute(sql)
                Card_Spell_Info = cursor.fetchall()

            case _ :
                print("Skill Issue")

    sql = f"SELECT * FROM decks"
    cursor.execute(sql)
    Deck_Info = cursor.fetchall()

    sql = f"SELECT Name FROM decks WHERE Deck_ID = %s"
    cursor.execute(sql, session['Deck_In_Use'])
    Deck_Name = (cursor.fetchone())['Name']

    sql = f"SELECT Card_ID FROM card_in_deck WHERE Deck_ID = %s"
    cursor.execute(sql, session['Deck_In_Use'])
    Deck_List= cursor.fetchall()
    Deck_Interior = [ids['Card_ID'] for ids in Deck_List]
    format_strings = ','.join(['%s'] * len(Deck_Interior))
    sql = f"SELECT * FROM cards WHERE Card_ID IN ({format_strings})"
    cursor.execute(sql, Deck_Interior)
    unique_cards = cursor.fetchall()
    card_dict = {card['Card_ID']: card for card in unique_cards}
    Deck_Content = [card_dict[card_id] for card_id in Deck_Interior]




    return render_template('Deck_Creation.html', cards_info=cards_info, Card_Spell_Info=Card_Spell_Info, Card_EGO_Info=Card_EGO_Info, Card_Sinner_Info=Card_Sinner_Info, Card_Ego_Gift_Info=Card_Ego_Gift_Info, Deck_Info=Deck_Info, Deck_Name=Deck_Name, Deck_Content=Deck_Content)

@app.route('/Card_viewer', methods=['GET', 'POST'])
def Card_viewer():
    Card_Ego_Gift_Info = []
    Card_Sinner_Info = []
    Card_Spell_Info = []
    Card_EGO_Info = []

    sql = f"SELECT * FROM cards"
    cursor.execute(sql)
    cards_info = cursor.fetchall()
    print(cards_info)

    for card in cards_info:
        match card['Card_Type'] :

            case "Sinner" :
                sql = f"SELECT * FROM sinners"
                cursor.execute(sql)
                Card_Sinner_Info = cursor.fetchall()
                print(Card_Sinner_Info)

            case "EGO_Gift" :
                sql = f"SELECT * FROM ego_gifts"
                cursor.execute(sql)
                Card_Ego_Gift_Info = cursor.fetchall()
                print(Card_Ego_Gift_Info)

            case "EGO" :
                sql = f"SELECT * FROM ego"
                cursor.execute(sql)
                Card_EGO_Info = cursor.fetchall()
                print(Card_EGO_Info)

            case "Spell" :
                sql = f"SELECT * FROM spell"
                cursor.execute(sql)
                Card_Spell_Info = cursor.fetchall()

            case _ :
                print("Skill Issue")


    return render_template('Card_Viewer.html', cards_info=cards_info, Card_Spell_Info=Card_Spell_Info, Card_EGO_Info=Card_EGO_Info, Card_Sinner_Info=Card_Sinner_Info, Card_Ego_Gift_Info=Card_Ego_Gift_Info)


if __name__ == '__main__':
    app.run()
