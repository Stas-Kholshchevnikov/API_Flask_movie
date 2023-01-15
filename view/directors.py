from flask_restx import Resource, Namespace
from flask import request

from dao.models.director import DirectorSchema
from implemented import director_service

director_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        """
        Фукнция получения всех режисеров из БД
        :return:
        """
        page = request.args.get("page")
        result = director_service.get_all(page)
        return directors_schema.dump(result), 200

@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        """
        Функция получения одного режисера из БД
        :param did:
        :return:
        """
        result = director_service.get_one(did)
        return director_schema.dump(result), 200
