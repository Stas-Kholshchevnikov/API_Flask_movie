from flask import request
from flask_restx import Resource, Namespace

from dao.models.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        page = request.args.get("page")
        result = genre_service.get_all(page)
        return genres_schema.dump(result), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self):
        result = genre_service.get_one()
        return genre_schema.dump(result), 200
