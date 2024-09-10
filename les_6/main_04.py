from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn as uv


app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50) # ... - часть синтаксиса. Обязательное поле. title='Name' - используется в документации /docs, /redoc
    price: float = Field(..., title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10) # default - пропущено, но воспринимается как значение по умолчанию


@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}


if __name__ == '__main__':
    uv.run('main_04:app', host='127.0.0.1', port=8000, reload=True)