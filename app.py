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
def hello_world():  # put application's code here
    return 'Hello World!'


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
        print(sinner_id)
        sinner_id = sinner_id['LAST_INSERT_ID()']
        sql = "INSERT INTO sinners (Card_ID, Name, Sinner, Cost, Attack, Defense_type, Defense_value, Speed, Stagger, Life, abilities, Text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (sinner_id, name, sinner, cost, atk, def_type, def_value, speed, stagger, life, abilities, text))
        connection.commit()
    return render_template('Sinner_Creation.html')


if __name__ == '__main__':
    app.run()
