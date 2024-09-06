# Создание конечных точек API

# FastAPI позволяет легко создавать конечные точки (endpoints) API для взаимодействия с клиентами.
# Рассмотрим, как определять конечные точки, работать с параметрами запроса и путями URL, а также форматировать ответы API.

    # Определение конечных точек API
    # Работа с параметрами запроса и путями URL
    # Форматирование ответов API
        # HTML текст
        # JSON объект
    # Динамический HTML через шаблонизатор Jinja



# Определение конечных точек API
# Конечная точка API — это URL-адрес, по которому клиент может отправлять запросы к серверу. В FastAPI определение конечных точек происходит с помощью декораторов.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # работает автоматическая валидация
async def read_item(item_id: int):
    return {"item_id": item_id}