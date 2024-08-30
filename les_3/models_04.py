# Модель базы данных

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model): # наследуется от класса Model, который находится внутри объекта db
    id = db.Column(db.Integer, primary_key=True) # первичный ключ
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    posts = db.relationship('Post', backref='author', lazy=True) # новая строка, backref - обратная ссылка, lazy - ленивый режим. 

    def __repr__(self):
        return f'User({self.username}, {self.email})'
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'Post({self.title}, {self.content})'