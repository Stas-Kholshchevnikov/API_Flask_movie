from const import COUNT_RECORDS
from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self, page):
        if page is not None:
            return self.dao.get_by_page(int(page), COUNT_RECORDS)
        else:
            return self.dao.get_all()
