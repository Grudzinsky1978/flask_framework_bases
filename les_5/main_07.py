# Валидация данных в запросах и ответах

# Автоматически делается с помощью модуля pydantic

from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

...