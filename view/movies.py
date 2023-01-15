from flask import request
from flask_restx import Namespace, Resource

from dao.models.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        """
        Функция вывода всех фильмов из БД
        :return:
        """
        status = request.args.get("status")
        page = request.args.get("page")
        data = {
            "status": status,
            "page": page
        }
        result = movie_service.get_all(data)
        return movies_schema.dump(result), 200


@movie_ns.route("/<int:uid>")
class MovieView(Resource):
    def get(self, uid):
        """
        Функция вывода одного фильма из БД
        :param uid:
        :return:
        """
        result = movie_service.get_one(uid)
        return movie_schema.dump(result), 200
