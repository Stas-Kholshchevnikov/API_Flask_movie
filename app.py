from flask import Flask
from flask_restx import Api

from config import Config
from create_db import make_db
from setup_db import db
from view.authorization import auth_ns
from view.directors import director_ns
from view.genres import genre_ns
from view.movies import movie_ns
from view.users import user_ns


def create_app(config_object):
    """
    Создание app
    :param config_object:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_params(app)
    return app


def register_params(app):
    """
    Создание параметров для app
    :param app:
    :return:
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


def create_table(app):
    """
    Функция первичного заполнения БД
    :param app:
    :return:
    """
    with app.app_context():
        make_db()


app = create_app(Config)
app.debug = True
#create_table(app)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

