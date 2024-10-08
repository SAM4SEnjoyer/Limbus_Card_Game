import pymysql
from flask import Flask, render_template, request

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

@app.route('/Ego_Gift_Creation', methods=['GET', 'POST'])
def Ego_Gift_Creation():

    if request.method == 'POST' and 'Name' in request.form and 'Cost' in request.form and 'Ability' in request.form and 'Ability_text' in request.form:
        name = request.form['Name']
        cost = request.form['Cost']
        ability = request.form['Ability']
        Ability_text = request.form['Ability_text']
        sql = "INSERT INTO Cards (Name, Card_Type) VALUES (%s, %s)"
        cursor.execute(sql, (name, "EGO_Gift"))
        connection.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        ego_gift_id = cursor.fetchone()
        ego_gift_id = ego_gift_id['LAST_INSERT_ID()']
        sql = "INSERT INTO ego_gifts (Card_ID, Name, Cost, ability, Ability_text) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(ego_gift_id, name, cost, ability, Ability_text))
        connection.commit()
    return render_template('Ego_Gift_Creation.html')

@app.route('/Sinner_Creation', methods=['GET', 'POST'])
def Sinner_Creation():
    if request.method == 'POST' and request.form['Name'] and request.form['Sinner'] and request.form['Cost'] and request.form['Attack'] and request.form['Speed'] and request.form['Defense_type'] and request.form['Defense_value'] and request.form['Stagger'] and request.form['Life']:
        name = request.form['Name']
        sinner = request.form['Sinner']
        cost = request.form['Cost']
        atk = request.form['Attack']
        speed = request.form['Speed']
        def_value = request.form['Defense_value']
        def_type = request.form['Defense_type']
        stagger = request.form['Stagger']
        life = request.form['Life']
        abilities = request.form['abilities']
        text = request.form['Text']
        sql = "INSERT INTO Cards (Name, Card_Type) VALUES (%s, %s)"
        cursor.execute(sql, (name, "Sinner"))
        connection.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        sinner_id = cursor.fetchone()
        sinner_id = sinner_id['LAST_INSERT_ID()']
        sql = "INSERT INTO sinners (Card_ID, Name, Sinner, Cost, Attack, Defense_type, Defense_value, Speed, Stagger, Life, abilities, Text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (sinner_id, name, sinner, cost, atk, def_type, def_value, speed, stagger, life, abilities, text))
        connection.commit()
    return render_template('Sinner_Creation.html')

@app.route('/EGO_Creation', methods=['GET', 'POST'])
def EGO_Creation():
    if request.method == 'POST' and request.form['Name'] and request.form['Sinner_name'] and request.form['Cost'] and request.form['Damage'] and request.form['Passive'] and request.form['Passive_text'] and request.form['Target_Number']:
        name = request.form['Name']
        sinner = request.form['Sinner_name']
        cost = request.form['Cost']
        dmg = request.form['Damage']
        ability = request.form['Ability']
        ability_text = request.form['Ability_text']
        passive = request.form['Passive']
        passive_text = request.form['Passive_text']
        target_num = request.form['Target_Number']
        sql = "INSERT INTO Cards (Name, Card_Type) VALUES (%s, %s)"
        cursor.execute(sql, (name, "EGO"))
        connection.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        ego_id = cursor.fetchone()
        ego_id = ego_id['LAST_INSERT_ID()']
        sql = "INSERT INTO ego (Card_ID, Name, Cost, Ability, Ability_text, Passive, Passive_text, Sinner_name, Damage, Target_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (ego_id, name, cost, ability, ability_text, passive, passive_text, sinner, dmg, target_num))
        connection.commit()
    return render_template('EGO_Creation.html')

@app.route('/Spell_Creation', methods=['GET', 'POST'])
def Spell_Creation():
    if request.method == 'POST' and request.form['Name'] and request.form['Hero'] and request.form['ability'] and request.form['Text'] and request.form['Cost']:
        name = request.form['Name']
        cost = request.form['Cost']
        ability = request.form['ability']
        text = request.form['Text']
        hero = request.form['Hero']
        sql = "INSERT INTO Cards (Name, Card_Type) VALUES (%s, %s)"
        cursor.execute(sql, (name, "Spell"))
        connection.commit()
        sql = "SELECT LAST_INSERT_ID()"
        cursor.execute(sql)
        spell_id = cursor.fetchone()
        spell_id = spell_id['LAST_INSERT_ID()']
        sql = "SELECT Hero_ID FROM heroes WHERE Name = %s"
        cursor.execute(sql, (hero))
        hero_id = cursor.fetchone()
        hero_id = hero_id['Hero_ID']
        sql = "INSERT INTO spell (Card_ID, Cost, ability, Name, Text, Hero_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (spell_id, cost, ability, name, text, hero_id))
        connection.commit()
    return render_template('Spell_Creation.html')


if __name__ == '__main__':
    app.run()
