import abc
from typing import List
from datetime import date

from flix.domain.model import Director, Genre, Actor, Movie, Review, User, WatchList


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """ Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds a Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, title) -> Movie:
        """ Returns the Movie with title from the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies(self) -> List[Movie]:
        """ Returns the movies stored in the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self) -> int:
        """ Returns the number of movies stored in the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """ Adds a Director to the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        """ Returns the directors stored in the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the genres stored in the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """ Adds an Actor to the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Genre]:
        """ Returns the actors stored in the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Review to the repository.

        If the Review doesn't have bidirectional links with an Movie and a User, this method raises a
        RepositoryException and doesn't update the repository.
        """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Comment not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Comment not correctly attached to an Movie')

    @abc.abstractmethod
    def get_reviews(self) -> List[Review]:
        """ Returns the reviews stored in the repository """
        raise NotImplementedError
