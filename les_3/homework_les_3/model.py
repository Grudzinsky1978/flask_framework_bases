# Модель

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=False, nullable=False)
    usersurname = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passw = db.Column(db.String(120), unique=True, nullable=False)
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User({self.usersurname}, {self.username}, {self.email}, {self.passw})'