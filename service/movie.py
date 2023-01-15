from const import COUNT_RECORDS
from dao.movie import MovieDAO


class MovieService:
    """
    Сервичс для обработки операций над таблицей movies
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        """
        Функция получения одной записи
        :param mid:
        :return:
        """
        return self.dao.get_one(mid)

    def get_all(self, data):
        """
        Функция получения всех записей
        :param data:
        :return:
        """
        if data["status"] == "new" and data["page"] is not None:
            return self.dao.get_sort_by_page(int(data["page"]), COUNT_RECORDS)
        elif data["status"] == "new":
            return self.dao.get_sort()
        elif data["page"] is not None:
            return self.dao.get_by_page(int(data["page"]), COUNT_RECORDS)
        else:
            return self.dao.get_all()
