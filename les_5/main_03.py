# Обработка HTTP-запросов

# GET - получение ресурсов с сервера
# POST - отрпавка данных на сервер
# PUT - изменение имеющихся данных
# DELETE - удаление данных


import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {'Hello,': 'World!'}