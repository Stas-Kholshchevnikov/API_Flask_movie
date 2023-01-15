from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    """
    Модель данных для таблцы movies
    """
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(), nullable=False)
    trailer = db.Column(db.String(), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    Схема данных для таблицы movies
    """
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    genre = fields.Pluck("GenreSchema", "name")
    director_id = fields.Int()
    director = fields.Pluck("DirectorSchema", "name")
