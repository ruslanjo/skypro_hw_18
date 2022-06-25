from app.dao.models.movies import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def get_movie_by_one_filter(self, db_column, condition):
        return self.session.query(Movie)\
                                .filter(getattr(Movie, db_column) == condition).all()

    '''def get_movie_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()'''

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie_id):
        movie = self.get_movie_by_id(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie
