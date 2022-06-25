from app.dao.movies_dao import MoviesDAO


class MovieService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_movie_by_id(self, movie_id):
        return self.dao.get_movie_by_id(movie_id)

    def get_movie_by_one_filter(self, data):
        '''data - объект request.args, в котором д.б. словарь с одним ключом и значением'''
        db_column = list(data.keys())[0]
        condition = list(data.values())[0]

        # код ниже обрабатывает случаи, когда в request.args поступают де-факто числа
        try:
            condition = int(condition)
        except ValueError:
            return self.dao.get_movie_by_one_filter(db_column, condition)
        else:
            return self.dao.get_movie_by_one_filter(db_column, condition)


    def create(self, data):
        self.dao.create(data)

    def update(self, movie_id, data):
        movie = self.get_movie_by_id(movie_id)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)
        return movie

    def update_partial(self, movie_id, data):
        movie = self.get_movie_by_id(movie_id)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)
        return movie

    def delete(self, movie_id):
        self.dao.delete(movie_id)

