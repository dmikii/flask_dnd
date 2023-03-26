from settings import DATABASE, DB_USER, DB_PASSWORD
from main import create_app

app = create_app(database = DATABASE, db_user = DB_USER, db_password = DB_PASSWORD)

app.run(debug = True)