from flask import Flask
import psycopg2
import json

app = Flask(__name__)

conn = psycopg2.connect(database = 'monsters_db', user = 'kdd', password = 'kdd')

@app.route('/')
def index():
    return "Welcome to DnD_Flask"

@app.route('/monsters')
def monsters():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM monsters')
    results = cursor.fetchall()
    return json.dumps(results, default=str)

app.run(debug = True)