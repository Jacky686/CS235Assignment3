import pytest

from flix.adapters.database_repository import SqlAlchemyRepository
from flix.domain.model import Director, Genre, Actor, Movie, User, Review, WatchList
from flix.adapters.repository import RepositoryException


def test_repository_can_add_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = User('Dave', '123456789')
    repo.add_user(user)

    repo.add_user(User('Martin', '123456789'))

    user2 = repo.get_user('dave')

    assert user2 == user and user2 is user


def test_repository_can_retrieve_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = repo.get_user('prince')
    assert user is None


def test_repository_can_add_and_get_movie(in_memory_repo):
    in_memory_repo.add_movie(Movie("Ice Age", 2002))

    assert in_memory_repo.get_movie("Ice Age") == Movie("Ice Age", 2002)

    assert in_memory_repo.get_movie("Guardians of the Galaxy") == Movie("Guardians of the Galaxy", 2014)


def test_repository_does_not_get_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie("test movie")

    assert movie is None


def test_repository_can_get_all_movies(in_memory_repo):
    movies = in_memory_repo.get_movies()
    assert len(movies) == 100


def test_repository_can_get_number_of_movies(in_memory_repo):
    assert in_memory_repo.get_number_of_movies() == 100


def test_repository_can_add_and_get_genres(in_memory_repo):
    genre = Genre("Horror")
    in_memory_repo.add_genre(genre)

    assert (genre in in_memory_repo.get_genres()) is True

    assert len(in_memory_repo.get_genres()) == 19


def test_repository_can_add_and_get_actors(in_memory_repo):
    actor = Actor("Matt Damon")
    in_memory_repo.add_actor(actor)

    assert (actor in in_memory_repo.get_actors()) is True

    assert len(in_memory_repo.get_actors()) == 321


def test_repository_can_add_and_get_reviews(in_memory_repo):
    review = Review(User("Bob12", "password888"), Movie("Ice Age", 2002), "Great", 8)
    in_memory_repo.add_review(review)

    reviews = in_memory_repo.get_reviews()
    assert reviews[0].user == User("Bob12", "password888")
    assert reviews[0].movie == Movie("Ice Age", 2002)
    assert reviews[0].review_text == "Great"
    assert reviews[0].rating == 8
