from app.dao.models.directors import Director


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_director_by_id(self, dir_id):
        return self.session.query(Director).get(dir_id)
