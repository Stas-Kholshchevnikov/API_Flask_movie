from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    """
    Модель данных для таблицы users
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String())
    surname = db.Column(db.String())
    favorite_genre = db.Column(db.Integer, db.ForeignKey('genres.id'))


class UserSchema(Schema):
    """
    Схема данных для таблицы users
    """
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Pluck("GenreSchema", "name")

