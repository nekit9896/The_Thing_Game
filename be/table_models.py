from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from be.app import app

db = SQLAlchemy(app)


class User(UserMixin, db.Model):  # Модель пользователя
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    mail = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)