import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = 'sqlite:///mydatabase.db' # В корневой директории
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL) # переменная. Из модуля databases используем класс Database, который получает адрес в константе

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users', # название таблицы
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True), # столбцы (колонки). ID формируется автоматически. Первичный ключ
    sqlalchemy.Column('name', sqlalchemy.String(32)),
    sqlalchemy.Column('email', sqlalchemy.String(128))
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False} # Эти ключ и значение нужны для того, чтобы работать с sqlite БД (в одном файле). Для других - не обязательно
    ) # формируем движок. Функция create_engine
metadata.create_all(engine) # формирование всех таблиц (таблицы сформированы)


app = FastAPI()


class UserIn(BaseModel): # когда вносим данные, ID не нужен (он пока неизвестен и присваивается автоматически)
    name: str = Field(max_length=32) # те же ограничения
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


@app.get('/fake_users/{count}') # заполнение таблицы фейковыми (демонстрационными) данными пользователей. Доступ к этой функциональности нужно не забыть потом заблокировать
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', email=f'mail{i}.@mail.ru') # запрос на добавление
        await database.execute(query)
    return {'message': f'{count} fake users create'}