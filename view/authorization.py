from flask_restx import Resource, Namespace

auth_ns = Namespace("auth")

@auth_ns.route("/register")
class Register(Resource):
    def post(self):
        pass

@auth_ns.route("/login")
class Login(Resource):
    def post(self):
        pass

    def put(self):
        pass

