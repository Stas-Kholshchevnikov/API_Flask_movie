from const import COUNT_RECORDS
from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self, page):
        if page is not None:
            return self.dao.get_by_page(int(page), COUNT_RECORDS)
        else:
            return self.dao.get_all()
