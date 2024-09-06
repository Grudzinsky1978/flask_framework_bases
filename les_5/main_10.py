# Работа с параметрами запроса и путями URL

from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}