# Автоматическая документация по API

# FastAPI обладает встроенным инструментом для автоматической документации API, который позволяет быстро и удобно ознакомиться с функциональностью приложения.
# Рассмотрим два варианта документации API: интерактивную документацию Swagger и альтернативную документацию ReDoc.

# Интерактивная документация Swagger
# http://localhost:8000/docs

# Альтернативная документация ReDoc
# http://localhost:8000/redoc


import logging
from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {'Hello,': 'World!'}

@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id =  {item_id}.')
    return {'item_id': item_id, 'item': item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id =  {item_id}.')
    return {'item_id': item_id}



# http://127.0.0.1:8000/docs