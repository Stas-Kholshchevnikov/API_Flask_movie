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
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, SECRET, algorithms=ALGO)
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper

