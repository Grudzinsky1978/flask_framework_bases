# Создание моделей

    # Определение классов моделей
    # Описание полей моделей
    # Создание связей между моделями
    # Создание таблиц в базе данных

# Модели класса - это по сути копии таблиц (в python модель, в базе данных - таблица)

from flask import Flask
from models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)