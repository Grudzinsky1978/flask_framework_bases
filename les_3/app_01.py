# Flask SQLAlchemy. Для работы с базами данных
# ОРМ - Объектно-реляционная модель, взаимодействие с базой данных не напрямую (с помощью запросов), а путём создания моделей данных

# Установка pip install Flask-SQLAlchemy

# Подключение к БД from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # инициализация приложения Flask, создания объекта приложения
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # в файл конфигурации своего приложения добавляется констаната и её значение (sqlite - внутри одного файла)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/database_name'
db = SQLAlchemy(app) # создан объект

# создаётся каталог instance

@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)