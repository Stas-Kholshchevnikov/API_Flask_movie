from dao.models.user import User


class UserDAO:
    """
    Класс работы с таблицей user базы данных
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """
        Поиск одного значения в тадлице БД
        :param uid:
        :return:
        """
        return self.session.query(User).get(uid)

    def get_all(self):
        """
        Выборка всех значений в таблице БД
        :return:
        """
        return self.session.query(User).all()

    def create(self, data):
        """
        Создание записи в таблице БД
        :param data:
        :return:
        """
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, data, user_email):
        """
        Обновление значений записи в таблице БД
        :param data:
        :param uid:
        :return:
        """
        self.session.query(User).filter(User.email == user_email).update(data)
        self.session.commit()
        return self.get_by_email(user_email)

    def get_by_email(self, user_email):
        """
        Выборка значения по совпадению имени пользователя
        :param user_name:
        :return:
        """
        return self.session.query(User).filter(User.email == user_email).one()
