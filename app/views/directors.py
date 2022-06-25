from flask_restx import Resource, Namespace
from app.container import directors_service
from app.dao.models.directors import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = directors_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200


@directors_ns.route('/<int:dir_id>')
class DirectorView(Resource):
    def get(self, dir_id):
        director = directors_service.get_by_id(dir_id)
        return DirectorSchema().dump(director), 200
