from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_sort(self):
        return self.session.query(Movie).order_by(Movie.year.desc()).all()

    def get_by_page(self, page, count_records):
        return self.session.query(Movie).paginate(page=page, per_page=count_records, error_out=True).items

    def get_sort_by_page(self, page, count_records):
        return self.session.query(Movie).order_by(Movie.year.desc()).paginate(page=page, per_page=count_records, error_out=True).items

