from flask import Flask, render_template
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

    sql = f"SELECT * FROM decks"
    cursor.execute(sql)
    Deck_Info = cursor.fetchall()




    return render_template('Deck_Creation.html', cards_info=cards_info, Card_Spell_Info=Card_Spell_Info, Card_EGO_Info=Card_EGO_Info, Card_Sinner_Info=Card_Sinner_Info, Card_Ego_Gift_Info=Card_Ego_Gift_Info, Deck_Info=Deck_Info)

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


    return render_template('Deck_Creation.html', cards_info=cards_info, Card_Spell_Info=Card_Spell_Info, Card_EGO_Info=Card_EGO_Info, Card_Sinner_Info=Card_Sinner_Info, Card_Ego_Gift_Info=Card_Ego_Gift_Info)


if __name__ == '__main__':
    app.run()
