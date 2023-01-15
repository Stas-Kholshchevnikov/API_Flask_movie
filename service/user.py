import base64

from dao.user import UserDAO
from const import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import hashlib


class UserService:
    """
    Сервис для обработки операци над таблицей user
    """
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self, data):
        """
        Функция создания записи
        :param data:
        :return:
        """
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def get_by_email(self, user_email):
        """
        Функция получения даннных пользовател по его email
        :param user_email:
        :return:
        """
        return self.dao.get_by_email(user_email)

    def update_info(self, data, user_email):
        """
        Функция обновления данных записи
        :param data:
        :param user_email:
        :return:
        """
        return self.dao.update(data, user_email)


    def update_password(self, data, user_email):
        """
        Функция смены паротя доступа для пользователя
        """
        data["password_1"] = self.get_hash(data["password_1"])
        user = self.dao.get_by_email(user_email)
        if data["password_1"] == user.password:
            new_pass = {}
            new_pass["password"] = self.get_hash(data["password_2"])
            self.dao.update(new_pass, user_email)
            return "The password has been successfully changed", 204
        else:
            return "Error: Invalid old password", 400


    def get_hash(self, password):
        """
        Функция получения хеша пароля
        :param password:
        :return:
        """
        password_digit = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('UTF-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(password_digit)