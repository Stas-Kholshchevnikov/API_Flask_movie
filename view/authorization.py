from flask import request
from flask_restx import Resource, Namespace

from dao.models.user import UserSchema
from implemented import auth_service, user_service

auth_ns = Namespace("auth")
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@auth_ns.route("/register")
class Register(Resource):
    def post(self):
        data = request.json
        result = user_service.create(data)
        return user_schema.dump(result), 201

@auth_ns.route("/login")
class Login(Resource):
    def post(self):
        data = request.json
        result = auth_service.get_token(data)
        return result

    def put(self):
        data = request.json
        result = auth_service.refresh_token(data)
        return result

