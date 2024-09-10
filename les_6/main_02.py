from pydantic import BaseModel, Field # Функция Field обращается к классу Param


class Item(BaseModel):
    name: str = Field(max_length=10) # Подставляем вместо значения по умолчанию


class User(BaseModel):
    age: int = Field(default=0)