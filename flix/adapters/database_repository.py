import csv
import os

from datetime import date
from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from werkzeug.security import generate_password_hash

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from flix.domain.model import Movie, Actor, Director, Genre, User, Review
from flix.adapters.repository import AbstractRepository


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if self.__session is not None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, user_name) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(_User__user_name=user_name).one()
        except NoResultFound:
            pass

        return user

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def get_movie(self, title) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(_Movie__title=title).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return movie

    def get_movies(self) -> List[Movie]:
        movies = self._session_cm.session.query(Movie).all()
        return movies

    def get_number_of_movies(self) -> int:
        number_of_movies = self._session_cm.query(Movie).count()
        return number_of_movies

    def add_director(self, director: Director):
        with self._session_cm as scm:
            scm.session.add(director)
            scm.commit()

    def get_directors(self) -> List[Director]:
        directors = self._session_cm.query(Director).all()
        return directors

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def get_genres(self) -> List[Genre]:
        genres = self._session_cm.query(Genre).all()
        return genres

    def add_actor(self, actor: Actor):
        with self._session_cm as scm:
            scm.session.add(actor)
            scm.commit()

    def get_actors(self) -> List[Genre]:
        actors = self._session_cm.query(Actor).all()
        return actors

    def add_review(self, review: Review):
        pass

    def get_reviews(self) -> List[Review]:
        pass


def generic_generator(filename, post_process=None):
    with open(filename) as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            if post_process is not None:
                row = post_process(row)
            yield row


def process_user(user_row):
    user_row[2] = generate_password_hash(user_row[2])
    return user_row


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = list()
        self.__dataset_of_directors = list()
        self.__dataset_of_genres = list()

    @property
    def dataset_of_movies(self) -> List[Movie]:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> List[Actor]:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> List[Director]:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> List[Genre]:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row["Title"]
                release_year = int(row["Year"])
                movie = Movie(title, release_year)

                movie.description = row["Description"]

                director = row["Director"]
                movie.add_director(Director(director))

                actors = row["Actors"].split(",")
                for actor in actors:
                    movie.add_actor(Actor(actor))

                genres = row["Genre"].split(",")
                for genre in genres:
                    movie.add_genre(Genre(genre))

                movie.runtime_minutes = int(row["Runtime (Minutes)"])

                try:
                    movie.external_rating = float(row["Rating"])
                except ValueError:
                    pass

                try:
                    movie.rating_votes = int(row["Votes"])
                except ValueError:
                    pass

                try:
                    movie.revenue_in_millions = float(row["Revenue (Millions)"])
                except ValueError:
                    pass

                try:
                    movie.metascore = int(row["Metascore"])
                except ValueError:
                    pass

                self.__dataset_of_movies.append(movie)
                # title = row['Title']
                # release_year = int(row['Year'])
                # print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1


def populate(engine: Engine, data_path: str):
    conn = engine.raw_connection()
    cursor = conn.cursor()

    insert_users = """
        INSERT INTO users (
        id, username, password)
        VALUES (?, ?, ?)"""
    cursor.executemany(insert_users, generic_generator(os.path.join(data_path, 'users.csv'), process_user))

    conn.commit()
    conn.close()


def populate_movies(session_factory, data_path: str):
    filename = os.path.join(data_path, 'Data1000Movies.csv')
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    session = session_factory()

    for movie in movie_file_reader.dataset_of_movies:
        session.add(movie)

    session.commit()
