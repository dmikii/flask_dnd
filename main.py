from flask import Flask
import psycopg2
import json
from settings import DATABASE, DB_USER, DB_PASSWORD
from monster import Monster

def create_app(database, db_user, db_password):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE = database,
        DB_USER = db_user,
        DB_PASSWORD = db_password
    )

    @app.route('/')
    def index():
        return "Welcome to DnD_Flask"

    @app.route('/monsters')
    def monsters():
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['DB_USER'], password = app.config['DB_PASSWORD'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM monsters')
        monsters = cursor.fetchall()
        monster_objs = [Monster(monster).__dict__ for monster in monsters]
        return json.dumps(monster_objs)

    @app.route('/monsters/<id>')
    def show_monster(id):
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['DB_USER'], password = app.config['DB_PASSWORD'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM monsters WHERE id = %s LIMIT 1;', (id,))
        results = cursor.fetchone()
        return json.dumps(results, default=str)

    return app