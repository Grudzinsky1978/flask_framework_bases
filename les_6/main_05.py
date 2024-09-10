# Работа с базой данных

# Создание подключения к базе данных

# Установка
    # pip install sqlalchemy
    # pip install databases[aiosqlite] # модуль для асинхронных запросов к БД

# Подключение
    # import databases
    # import sqlalchemy


# Создание API операций CRUD
# CRUD - Create, Read, Update, Delete - основные функции

# Работа с БД в CRUD операциях с SQLAlchemy и databases
# Для работы с базой данных в операциях CRUD с SQLAlchemy ORM нам необходимо сначала установить соединение с базой данных.
    # Создаём таблицы в БД, используя SQLAlchemy
    # Создаём модели для взаимодействия стаблицей в БД
    # Создаём цепочку CRUD, чтобы использовать HTTP запросы к БД



# Базовые настройки

import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = 'sqlite:///mydatabase.db' # В корневой директории
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL) # переменная. Из модуля databases используем класс Database, который получает адрес в константе

metadata = sqlalchemy.MetaData()

...


engine = sqlalchemy.create_engine(DATABASE_URL) # формируем движок. Функция create_engine
metadata.create_all(engine) # формирование всех таблиц (таблицы пока не созданы, создаётся только файл БД)


app = FastAPI()


@app.on_event("startup") # не по адресу, а по событию
async def startup():
    await database.connect() # асинхронный запрос подключения к БД

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()