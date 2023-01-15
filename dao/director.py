from dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """
        Получение одной записи из БД
        :param did:
        :return:
        """
        return self.session.query(Director).get(did)

    def get_all(self):
        """
        Получение всех записей из БД
        :return:
        """
        return self.session.query(Director).all()

    def get_by_page(self, page, count_records):
        """
        Получение всех записей из БД с пагинацией
        :param page:
        :param count_records:
        :return:
        """
        return self.session.query(Director).paginate(page=page, per_page=count_records, error_out=True).items
