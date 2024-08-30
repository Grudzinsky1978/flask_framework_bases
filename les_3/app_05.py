from flask import Flask
from models_05 import db, User, Post, Comment # Импорт моделей и объекта db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

@app.cli.command("init-db") # при появлении команды init-db запускается функция init_db()
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all() # создаются таблицы на основе моделей
    print('OK')



if __name__ == '__main__':
    app.run(debug=True)