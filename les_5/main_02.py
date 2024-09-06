# Создание базового приложения FastAPI

    # Содание модуля приложения
    # Настройка сервера маршрутизации
    # Запуск приложения


# Создание модуля приложения
# Рекомендуется название main

from fastapi import FastAPI

app = FastAPI()



@app.get('/')
async def read_root():
    return {'Hello': 'World!'}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}


# http://127.0.0.1:8000/items/42?q=text # стандартная отправка GET запроса, далее ключи и значения через &