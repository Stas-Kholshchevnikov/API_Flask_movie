from const import COUNT_RECORDS
from dao.genre import GenreDAO


class GenreService:
    """
    Сервис для обработки операций над таблицей genres
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        """
        Функция получения одной записи
        :param gid:
        :return:
        """
        return self.dao.get_one(gid)

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
