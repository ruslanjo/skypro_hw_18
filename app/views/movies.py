import json

from flask import request
from flask_restx import Resource, Namespace
from app.container import movies_service
from app.dao.models.movies import MovieSchema


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        req_args = request.args

        if len(req_args) > 0:
            movies = movies_service.get_movie_by_one_filter(req_args)
        else:
            movies = movies_service.get_all()
        return MovieSchema(many=True).dump(movies), 200

    def post(self):
        data = request.json
        movies_service.create(data)
        return json.dumps(data), 201


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = movies_service.get_movie_by_id(movie_id)
        return MovieSchema().dump(movie), 200

    def put(self, movie_id):
        data = request.json
        movies_service.update(movie_id, data)
        return '', 204

    def patch(self, movie_id):
        data = request.json
        movies_service.update_partial(movie_id, data)
        return '', 204

    def delete(self, movie_id):
        movies_service.delete(movie_id)
        return '', 204

