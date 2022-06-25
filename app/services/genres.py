from app.dao.genres_dao import GenresDAO


class GenreService:
    def __init__(self, dao: GenresDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, genre_id):
        return self.dao.get_genre_by_id(genre_id)
