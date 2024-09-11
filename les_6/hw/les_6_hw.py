from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
import uvicorn as uv
from datetime import datetime

from wtforms import PasswordField

DATABASE_URL = 'sqlite:///eshop.db'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(32)),
    sqlalchemy.Column('surname', sqlalchemy.String(32)),
    sqlalchemy.Column('email', sqlalchemy.String(128), unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(128))
)

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('product_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('product_name', sqlalchemy.String(128), unique=True),
    sqlalchemy.Column('description', sqlalchemy.Text),
    sqlalchemy.Column('price', sqlalchemy.Float)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('order_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('creator_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.user_id'), nullable=False),
    sqlalchemy.Column('prod_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.product_id'), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.now()),
    sqlalchemy.Column('order_status', sqlalchemy.Boolean, default=True)
)




engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
    )

metadata.create_all(engine)


app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class User(BaseModel):
    user_id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128, min_length=10, validate_default=EmailStr)
    password: str = Field(max_length=128, min_length=6, validate_default=PasswordField)


class ProductIn(BaseModel):
    product_name: str = Field(max_length=128)
    description: str = Field(max_length=64000)
    price: float = Field(ge=100, le=100000)


class Product(BaseModel):
    product_id: int
    product_name: str = Field(max_length=128)
    description: str = Field(max_length=64000)
    price: float = Field(ge=100, le=100000)




class OrderIn(BaseModel):
    creator_id: int
    prod_id: int


class Order(BaseModel):
    order_id: int
    created_at: datetime = Field(default=datetime.now())
    creator_id: int
    prod_id: int
    order_status: bool = Field(default=True)





@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, surname=user.surname, email=user.email, password=user.password) # user - модель pydentic, users - модель sqlalchemic
    last_record_id = await database.execute(query)
    return {**user.dict(), 'user_id': last_record_id}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.user_id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), 'user_id': user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {'message': 'Пользователь удалён'}



# ---------------------



@app.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(product_name=product.product_name, description=product.description, price=product.price)
    last_record_id = await database.execute(query)
    return {**product.dict(), 'product_id': last_record_id}


@app.get('/products/', response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get('/products/{product_id}', response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.product_id == product_id)
    return await database.fetch_one(query)


@app.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.product_id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), 'product_id': product_id}


@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.product_id == product_id)
    await database.execute(query)
    return {'message': 'Товар удалён'}



# ------------------------------


@app.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(creator_id=order.creator_id, prod_id=order.prod_id, created_at=datetime.now(), order_status=True)
    last_record_id = await database.execute(query)
    return {**order.dict(), 'order_id': last_record_id}


@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.order_id == order_id)
    return await database.fetch_one(query)


@app.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.order_id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), 'order_id': order_id}


@app.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.order_id == order_id)
    await database.execute(query)
    return {'message': 'Заказ удалён'}




if __name__ == '__main__':
    uv.run('les_6_hw:app', host='127.0.0.1', port=8000, reload=True)