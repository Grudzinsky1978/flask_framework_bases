# Удаление данных из таблицы БД

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


@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='John').first() # Создаём объект запроса (query), с фильтром. Найти нужно первое совпадение (first). Возвращаем в переменную user
    user.email = 'new_email@example.com' # Обращаемся к свойству email и присваиваем новое значение
    db.session.commit() # add не нужен, закрепляются новые данные
    print('Edit John mail in DB!')

# при запуске к файлу не должно быть обращения другой программы, иначе база данных блокируется для изменений

@app.cli.command("del-john")
def def_user():
    user = User.query.filter_by(username='John').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')



if __name__ == '__main__':
    app.run(debug=True)


# Лайфхак
# Обычно из БД информацию не удаляют, а добавляют колонку (Visisble или Is Visible), там сохраняют логическое значение по умолчанию True
# Для того, чтобы не отображать устаревшие данные, Visible присваивают False, фильтром выводят только Visible = True