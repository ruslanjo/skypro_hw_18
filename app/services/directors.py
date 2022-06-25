from app.dao.directors_dao import DirectorsDAO


class DirectorService:
    def __init__(self, dao: DirectorsDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, dir_id):
        return self.dao.get_director_by_id(dir_id)
