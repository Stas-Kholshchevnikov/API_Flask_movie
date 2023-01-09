from dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_page(self, page, count_records):
        return self.session.query(Genre).paginate(page=page, per_page=count_records, error_out=True).items
