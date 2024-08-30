# Работа с данными в базе данных
    # Создание
    # Изменение
    # Удаление
    # Получение данных
    #     фильтрация данных


from flask import Flask
from models_05 import db, User, Post, Comment # Импорт моделей и объекта db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

@app.cli.command("init-db") # при появлении команды init-db (вместе с flask) запускается функция init_db()
def init_db():
    db.create_all() # создаются таблицы на основе моделей
    print('OK')


@app.cli.command("add-john")
def add_user():
    user = User(username='John', email='john@example.com') # создаётся экземпляр класса User 
    db.session.add(user) # объект сессий в db (подключение), сетод add не добавляет, а как бы подвешивает транзакцию, добавляет в сессию
    db.session.commit() # здесь добавляются данные
    print('John add in DB!')




if __name__ == '__main__':
    app.run(debug=True)