import jwt
from flask import request, abort

from const import SECRET, ALGO


def auth_required(func):
    """
    Декоратор на проверку наличия access токена
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        decode_token(data)

        return func(*args, **kwargs)

    return wrapper


def decode_token(data):
    """
    Функиця декодирования токена
    :param data:
    :return:
    """

    token = data.split('Bearer ')[-1]

    try:
        token_info = jwt.decode(token, SECRET, algorithms=ALGO)
        user_email = token_info.get("email")
        return user_email
    except Exception:
        abort(401)

