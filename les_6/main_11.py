from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = 'sqlite:///mydatabase.db' # В корневой директории

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


# @app.get('/fake_users/{count}') # заполнение таблицы фейковыми (демонстрационными) данными пользователей. Доступ к этой функциональности нужно не забыть потом заблокировать
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}.@mail.ru') # запрос на добавление
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email) # user - модель pydentic, users - модель sqlalchemic
    # query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query) # асинхронный запрос
    return {**user.dict(), 'id': last_record_id}

# Связали: таблицу БД + модели FAST API. Сделали возможность передавать эти модели в записи в БД


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id) # c - колонка
    return await database.fetch_one(query)


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), 'id': user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}