from flask import request
from flask_restx import Resource, Namespace

from dao.models.user import UserSchema
from implemented import user_service
from service.decorators import auth_required, decode_token

user_ns = Namespace("users")

user_schema = UserSchema()

@user_ns.route("/")
class UserView(Resource):
    @auth_required
    def get(self):
        """
        Функция получения данных пользователя
        :return:
        """
        data = request.headers['Authorization']
        user_email = decode_token(data)
        user_info = user_service.get_by_email(user_email)
        return user_schema.dump(user_info), 200

    @auth_required
    def patch(self):
        """
        Функция обновления данных пользователя
        :return:
        """
        data = request.headers['Authorization']
        user_email = decode_token(data)
        data = request.json
        user_info = user_service.update_info(data, user_email)
        return user_schema.dump(user_info), 204


@user_ns.route("/password")
class UserUpdate(Resource):
    @auth_required
    def put(self):
        """
        Функция смены пароля пользователя
        :return:
        """
        data = request.headers['Authorization']
        user_email = decode_token(data)
        data = request.json
        result = user_service.update_password(data, user_email)
        return result
