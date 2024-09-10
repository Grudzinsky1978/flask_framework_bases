import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

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


@app.on_event("startup") # не по адресу, а по событию
async def startup():
    await database.connect() # асинхронный запрос подключения к БД

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()