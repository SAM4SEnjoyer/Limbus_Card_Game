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


@app.route('/Card_Creation', methods=['GET', 'POST'])
def Card_Creation():

    sql = "SELECT Name FROM Cards WHERE Card_ID=%s"
    cursor.execute(sql,(1,) )
    Card_Name = cursor.fetchone()
    print(Card_Name)

    if request.method == 'POST' and request.form['Card_Name'] and request.form['Card_Type']:
        name = request.form['Card_Name']
        Type = request.form['Card_Type']
        sql = "INSERT INTO Cards (Name, Card_Type) VALUES (%s, %s)"
        cursor.execute(sql, (name, Type))
        connection.commit()



    return render_template('Card_Creation.html', Card_Name=Card_Name['Name'])


if __name__ == '__main__':
    app.run()
