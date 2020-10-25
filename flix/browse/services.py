from typing import List, Iterable

from flix.adapters.repository import AbstractRepository
from flix.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList


def get_movies(repo: AbstractRepository):
    movies = repo.get_movies()

    if movies is None:
        pass

    return movies
