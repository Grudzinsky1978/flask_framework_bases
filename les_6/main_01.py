# Введение в модели данных в FastAPI

# Pydantic — это библиотека для валидации данных и сериализации объектов Python.
#     Она используется в FastAPI для валидации данных, получаемых из запросов, и генерации документации API на основе моделей данных.

# Модель данных — это класс Python, определяющий поля и их типы для описания данных.
#     Для определения моделей данных в FastAPI используется класс BaseModel из модуля pydantic.
#     Классы моделей содержат поля, которые описывают структуру данных.


from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None # Необязательное. Можно прописать False, тогда, в случае игнорирования, присваивалось данное значение по умолчанию

class User(BaseModel):
    username: str
    full_name: str = None # Необязательное

class Order(BaseModel):
    items: List[Item] # одна модель указывает на другую. Внутри списка каждый элемент должен быть экземпляром созданного нами класса Item
    user: User # Тоже модель класса, созданного ранее

