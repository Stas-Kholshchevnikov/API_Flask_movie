from dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        """
        Получение одной записи из БД
        :param gid:
        :return:
        """
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """
        Получение всех записей из БД
        :return:
        """
        return self.session.query(Genre).all()

    def get_by_page(self, page, count_records):
        """
        Получение всех записей из БД с пагинацией
        :param page:
        :param count_records:
        :return:
        """
        return self.session.query(Genre).paginate(page=page, per_page=count_records, error_out=True).items
