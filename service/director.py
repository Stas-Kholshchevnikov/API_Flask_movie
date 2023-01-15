from const import COUNT_RECORDS
from dao.director import DirectorDAO


class DirectorService:
    """
    Сервис для обработки операция над таблицей directors
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """
        Функция полученяи одной записи
        :param did:
        :return:
        """
        return self.dao.get_one(did)

    def get_all(self, page):
        """
        Функция получения всех записей
        :param page:
        :return:
        """
        if page is not None:
            return self.dao.get_by_page(int(page), COUNT_RECORDS)
        else:
            return self.dao.get_all()
