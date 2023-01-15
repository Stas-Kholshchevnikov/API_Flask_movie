class Config(object):
    """
    Класс конфигураций app
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False}
