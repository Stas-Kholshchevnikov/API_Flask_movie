from const import COUNT_RECORDS
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, data):
        if data["status"] == "new" and data["page"] is not None:
            return self.dao.get_sort_by_page(int(data["page"]), COUNT_RECORDS)
        elif data["status"] == "new":
            return self.dao.get_sort()
        elif data["page"] is not None:
            return self.dao.get_by_page(int(data["page"]), COUNT_RECORDS)
        else:
            return self.dao.get_all()
