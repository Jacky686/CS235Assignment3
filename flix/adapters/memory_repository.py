import os
import csv
from datetime import date, datetime
from typing import List

from werkzeug.security import generate_password_hash

from flix.adapters.repository import AbstractRepository, RepositoryException
from flix.domain.model import Movie, Actor, Director, Genre, User, Review


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._users = list()
        self._reviews = list()

        self._movies = list()
        self._actors = list()
        self._directors = list()
        self._genres = list()

    def add_user(self, user: User):
        print(user)
        self._users.append(user)

    def get_user(self, username) -> User:
        username = username.strip().lower()
        return next((user for user in self._users if user.user_name == username), None)

    def add_movie(self, movie: Movie):
        self._movies.append(movie)

    def get_movie(self, title) -> Movie:
        return next((movie for movie in self._movies if movie.title == title), None)

    def get_movies(self) -> List[Movie]:
        return self._movies

    def get_number_of_movies(self) -> int:
        return len(self._movies)

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_directors(self) -> List[Director]:
        return self._directors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self._genres

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actors(self) -> List[Actor]:
        return self._actors

    def add_review(self, review: Review):
        # super().add_review(review)
        self._reviews.append(review)

    def get_reviews(self) -> List[Review]:
        return self._reviews


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
                movie.director = Director(director)
                if Director(director) not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(Director(director))

                actors = row["Actors"].split(",")
                for actor in actors:
                    movie.add_actor(Actor(actor))
                    if Actor(actor) not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(Actor(actor))

                genres = row["Genre"].split(",")
                for genre in genres:
                    movie.add_genre(Genre(genre))
                    if Genre(genre) not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(Genre(genre))

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


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def populate(data_path: str, repo: MemoryRepository):
    users = load_users(data_path, repo)

    path = os.path.join(data_path, 'Data1000Movies.csv')

    movie_file_reader = MovieFileCSVReader(path)
    movie_file_reader.read_csv_file()

    for movie in movie_file_reader.dataset_of_movies:
        repo.add_movie(movie)

    for actor in movie_file_reader.dataset_of_actors:
        repo.add_actor(actor)

    for director in movie_file_reader.dataset_of_directors:
        repo.add_director(director)

    for genre in movie_file_reader.dataset_of_genres:
        repo.add_genre(genre)
