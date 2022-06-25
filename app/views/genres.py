from flask_restx import Resource, Namespace
from app.container import genres_service
from app.dao.models.genres import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresViews(Resource):
    def get(self):
        genres = genres_service.get_all()
        return GenreSchema(many=True).dump(genres), 200



@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = genres_service.get_by_id(genre_id)
        return GenreSchema().dump(genre), 200
