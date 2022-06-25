from setup_db import db

from app.dao.movies_dao import MoviesDAO
from app.services.movies import MovieService

from app.dao.genres_dao import GenresDAO
from app.services.genres import GenreService

from app.dao.directors_dao import DirectorsDAO
from app.services.directors import DirectorService


movies_dao = MoviesDAO(db.session)
movies_service = MovieService(movies_dao)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorService(directors_dao)

genres_dao = GenresDAO(db.session)
genres_service = GenreService(genres_dao)
