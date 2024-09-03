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
def menu():  # put application's code here
    return render_template('menu.html')



if __name__ == '__main__':
    app.run()
