from app.dao.models.genres import Genre


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_genre_by_id(self, genre_id):
        return self.session.query(Genre).get(genre_id)
