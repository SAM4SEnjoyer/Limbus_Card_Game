from flask import *
import pymysql


from Functions import draw, fullClear, init, discard

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

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form:
        Name = request.form['Name']
        cursor.execute('SELECT * FROM users WHERE Name = %s',
                       (Name, ))
        account = cursor.fetchone()
        if account:
            session['Connected'] = True
            session['Account_Name'] = account['Name']
            session['Account_ID'] = account['User_ID']
            return redirect(url_for('menu'))
        else:
            msg = 'Wrong name'
    return render_template('login.html', msg=msg)


@app.route('/Register', methods=['GET', 'POST'])
def Register():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form:
        Name = request.form['Name']
        cursor.execute('SELECT * FROM users WHERE Name = %s', Name)
        account = cursor.fetchone()
        if account:
            msg = 'This account already exists'
        else:
            cursor.execute('INSERT INTO users (Name) VALUES (%s)', (Name))
            connection.commit()
            cursor.execute('SELECT * FROM users WHERE Name = %s', Name)
            account = cursor.fetchone()
            session['Connected'] = True
            session['Account_Name'] = account['Name']
            session['Account_ID'] = account['User_ID']
            return redirect(url_for('menu'))
    return render_template('Register.html', msg=msg)


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/Choose_Deck', methods=['GET', 'POST'])
def choose_deck():
    msg=''
    if request.method == 'POST' and 'deck_chosen' in request.form:
        deck_chosen = request.form['deck_chosen']
        sql = "SELECT * FROM decks WHERE Deck_ID = %s;"
        cursor.execute(sql, deck_chosen)
        deck_chosen = cursor.fetchone()

        if deck_chosen['Number_of_Cards'] == 40:
            sql = "INSERT INTO decks (Name, Hero_ID, Number_of_Cards, Type) VALUES (%s, %s, %s, 'in_game')"
            cursor.execute(sql, (deck_chosen['Name'], deck_chosen['Hero_ID'], deck_chosen['Number_of_Cards']))
            connection.commit()
            sql = "SELECT Card_ID FROM card_in_deck WHERE Deck_ID = %s"
            cursor.execute(sql, deck_chosen['Deck_ID'])
            deck_list = cursor.fetchall()
            sql = "SELECT LAST_INSERT_ID()"
            cursor.execute(sql)
            id = cursor.fetchone()['LAST_INSERT_ID()']
            for card in deck_list:
                sql = "INSERT INTO card_in_deck (Card_ID, Deck_ID) VALUES (%s, %s)"
                cursor.execute(sql, (card['Card_ID'], id))
                connection.commit()
            session['Deck_Used_ID']=id
            return redirect(url_for('play'))
        else:
            msg = 'Too many cards or too few cards'

    sql = f"SELECT * FROM decks"
    cursor.execute(sql)
    Deck_Info = cursor.fetchall()
    session['Max_Light'] = 0
    session['Beginning_of_game'] = True

    return render_template('Choose_Deck.html', msg=msg, Deck_Info=Deck_Info)

@app.route('/Play', methods=['GET', 'POST'])
def play():
    Cards_in_hand = []
    Cards_in_hand_IDs = []
    Cards_in_board = []
    Users_in_Game = []
    Card_Ego_Gift_Info = []
    Card_Sinner_Info = []
    Card_Spell_Info = []
    Card_EGO_Info = []
    Hand_Card_Data = []
    Cards_in_hand_2 = []


    if session['Beginning_of_game']:
        session['Must_Discard'] = False
        session['Beginning_of_game'] = False
        sql = "INSERT INTO game (State) VALUES (%s)"
        cursor.execute(sql, 'Initialisation')
        connection.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        session['Game_ID'] = cursor.fetchone()['LAST_INSERT_ID()']
        sql = "INSERT INTO user_in_game (User_ID, Game_ID) VALUES (%s, %s)"
        cursor.execute(sql, (session['Account_ID'], session['Game_ID']))
        connection.commit()

    sql = "SELECT * FROM game WHERE Game_ID = %s"
    cursor.execute(sql, session['Game_ID'])
    game = cursor.fetchone()

    match game['State']:
        case "Initialisation":
            init(cursor, connection, session)
            session['Max_Light']=0
            sql = "UPDATE Game SET State=%s WHERE Game_ID = %s"
            cursor.execute(sql, ('Upkeep', session['Game_ID']))
            connection.commit()
        case "Upkeep":
            draw(session['Hand_Used_ID'], session['Deck_Used_ID'], 1, cursor, connection, session)
            session['Max_Light'] = session['Max_Light']+1
            session['Light'] = session['Max_Light']
            sql = "UPDATE Game SET State=%s WHERE Game_ID = %s"
            cursor.execute(sql, ('Turn_End', session['Game_ID']))
            connection.commit()
            # Fin des effets durant husqu'au prochain tour
            # Déclenchement des effets de début de tour
        case "Main":
            print("main")
        case "Turn_End":
            if session['Number_in_Hand']>7:
                print('Yup')
                session['Must_Discard'] = True
                if request.method == 'POST' and 'Choice_Discard' in request.form:
                    Card_ID = request.form['Choice_Discard']
                    discard(Card_ID, cursor, connection)
            else:
                sql = "UPDATE Game SET State=%s WHERE Game_ID = %s"
                cursor.execute(sql, ('Upkeep', session['Game_ID']))
                connection.commit()
            # Fin des effets de tour
            # Déclenchement des effets de fin tour
            # Passer la main
        case _ :
            print("pop")


    sql = f"SELECT * FROM cards_in_hand WHERE Hand_ID=%s"
    cursor.execute(sql, session["Hand_Used_ID"])
    Cards_in_hand = cursor.fetchall()

    sql = "SELECT * FROM cards"
    cursor.execute(sql)
    Cards_in_hand_2 = cursor.fetchall()

    for cards in Cards_in_hand:
        for card_2 in Cards_in_hand_2:
            if cards['Card_ID'] == card_2['Card_ID']:
                Hand_Card_Data.append({**cards, **card_2})

    print(Hand_Card_Data)

    for cards in Hand_Card_Data:
        match cards['Card_Type'] :

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

    sql = "SELECT * FROM user_in_game WHERE Game_ID = %s"
    cursor.execute(sql, 1)
    Users_in_Game = cursor.fetchall()


    if request.method=='POST':
        fullClear(cursor, connection)
        redirect(url_for('menu'))

    # sql = "SELECT * FROM cards_in_hand WHERE User_ID = %s"
    # cursor.execute(sql, session['Account_ID'])
    # Cards_in_hand = cursor.fetchall()
    #
    # sql = "SELECT * FROM cards_in_board WHERE User_ID = %s"
    # cursor.execute(sql, session['Account_ID'])
    # Cards_in_board = cursor.fetchall()

    return render_template('Play.html', Cards_in_hand=Hand_Card_Data, Cards_in_board=Cards_in_board, Users_in_Game=Users_in_Game,
                           Card_Spell_Info=Card_Spell_Info, Card_EGO_Info=Card_EGO_Info, Card_Sinner_Info=Card_Sinner_Info, Card_Ego_Gift_Info=Card_Ego_Gift_Info,
                           Must_Discard=session['Must_Discard'])

@app.route('/Deck_Creation', methods=['GET', 'POST'])
def Deck_Creation():
    Card_Ego_Gift_Info = []
    Card_Sinner_Info = []
    Card_Spell_Info = []
    Card_EGO_Info = []
    Deck_Info = []
    Deck_Content = []

    sql = f"SELECT * FROM cards"
    cursor.execute(sql)
    cards_info = cursor.fetchall()


    if not 'Deck_In_Use' in session.keys():

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
        sql = f"SELECT Number_of_Cards FROM decks WHERE Deck_ID = %s"
        cursor.execute(sql, session['Deck_In_Use'])
        number=cursor.fetchone()['Number_of_Cards']+1
        sql = f"UPDATE decks SET Number_of_Cards = %s WHERE Deck_ID = %s"
        cursor.execute(sql, (number, session['Deck_In_Use']))
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
        sql = f"SELECT Number_of_Cards FROM decks WHERE Deck_ID = %s"
        cursor.execute(sql, session['Deck_In_Use'])
        number = cursor.fetchone()['Number_of_Cards'] - 1
        sql = f"UPDATE decks SET Number_of_Cards = %s WHERE Deck_ID = %s"
        cursor.execute(sql, (number, session['Deck_In_Use']))
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
    if Deck_List:
        Deck_Interior = [ids['Card_ID'] for ids in Deck_List]
        format_strings = ','.join(['%s'] * len(Deck_Interior))
        sql = f"SELECT * FROM cards WHERE Card_ID IN ({format_strings})"
        cursor.execute(sql, Deck_Interior)
        unique_cards = cursor.fetchall()
        card_dict = {card['Card_ID']: card for card in unique_cards}
        Deck_Content = [card_dict[card_id] for card_id in Deck_Interior]


    return render_template('Deck_Creation.html', cards_info=cards_info, Card_Spell_Info=Card_Spell_Info, Card_EGO_Info=Card_EGO_Info, Card_Sinner_Info=Card_Sinner_Info, Card_Ego_Gift_Info=Card_Ego_Gift_Info, Deck_Info=Deck_Info, Deck_Name=Deck_Name, Deck_Content=Deck_Content)

@app.route('/Deck_Creator', methods=['GET', 'POST'])
def Deck_Creator():

    if request.method == 'POST':
        if request.form["Name"] and request.form["chosen_hero"]:
            name = request.form["Name"]
            hero_id = request.form["chosen_hero"]
            print(hero_id)
            sql = f"INSERT INTO decks (Name, Hero_ID, Number_of_Cards, Type) VALUES (%s, %s, 0, 'main')"
            cursor.execute(sql, (name, hero_id))
            connection.commit()
            sql = "SELECT LAST_INSERT_ID()"
            cursor.execute(sql)
            deck_ID = cursor.fetchone()['LAST_INSERT_ID()']
            sql = "SELECT card_ID FROM spell WHERE Hero_ID = %s"
            cursor.execute(sql, hero_id)
            spell_list = cursor.fetchall()
            spell_count = 0
            for card in spell_list:
                print(card)
                spell_count += 1
                sql = f"INSERT INTO card_in_deck (Card_ID, Deck_ID) VALUES (%s, %s)"
                cursor.execute(sql, (card['card_ID'], deck_ID))
                connection.commit()
            sql = f"UPDATE decks SET Number_of_Cards = %s WHERE Deck_ID = %s"
            cursor.execute(sql, (spell_count, deck_ID))
            connection.commit()
            session['Deck_In_Use'] = deck_ID
            return redirect(url_for('Deck_Creation'))


    print('lol')
    sql = f"SELECT * FROM heroes"
    cursor.execute(sql)
    Hero_List = cursor.fetchall()


    return render_template('Deck_Creator.html', Hero_List=Hero_List)



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