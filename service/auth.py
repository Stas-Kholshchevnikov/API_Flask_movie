from flask_restx import abort
from dao.user import UserDAO

from const import SECRET, ALGO
import datetime
import calendar
import jwt

from service.user import UserService


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_token(self, data):
        """
        функция получения пары токенов
        :param data:
        :return:
        """
        user_email = data.get("email")
        password_user = data.get("password")
        try:
            user = self.dao.get_by_email(user_email)
        except Exception:
            abort(401)

        if user.password != UserService.get_hash(user, password_user):
            abort(401)

        token_data = {
            "email": user.email,
            "name": user.name
                    }

        result = self.create_token(token_data)
        return result

    def refresh_token(self, data):
        """
        Функция обновления пары токенов
        :param data:
        :return:
        """
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        try:
            access_token_info = jwt.decode(access_token, SECRET, algorithms=ALGO)
            refresh_token_info = jwt.decode(refresh_token, SECRET, algorithms=ALGO)
        except Exception:
            abort(401)

        user_email = refresh_token_info.get("email")
        user = self.dao.get_by_email(user_email)

        token_data = {
            "email": user.email,
            "name": user.name
        }

        result = self.create_token(token_data)
        return result

    def create_token(self, token_data):
        """
        Создание пары токенов
        :param token_data:
        :return:
        """
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token_data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(token_data, SECRET, algorithm=ALGO)
        day10 = datetime.datetime.utcnow() + datetime.timedelta(days=10)
        token_data["exp"] = calendar.timegm(day10.timetuple())
        refresh_token = jwt.encode(token_data, SECRET, algorithm=ALGO)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token
                }

        return tokens
