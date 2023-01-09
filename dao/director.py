from dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_page(self, page, count_records):
        return self.session.query(Director).paginate(page=page, per_page=count_records, error_out=True).items
