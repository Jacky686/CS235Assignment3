from domainmodel.movie import Movie
from domainmodel.review import Review

from typing import List


class User:

    def __init__(self, user_name: str, password: str):
        if type(user_name) is str:
            self.__user_name = user_name.strip().lower()
        else:
            self.__user_name = None

        if type(password) is str:
            self.__password = password
        else:
            self.__password = None

        self.__watched_movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> List[Movie]:
        return self.__watched_movies

    @property
    def reviews(self) -> List[Review]:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if self.__user_name == other.__user_name:
            return True

        return False

    def __lt__(self, other):
        if self.__user_name < other.__user_name:
            return True

        return False

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if isinstance(movie, Movie) and movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review) and review not in self.__reviews:
            self.__reviews.append(review)


class TestUser:

    def test_init(self):
        pass
        # user1 = User('Martin', 'pw12345')
        # user2 = User('Ian', 'pw67890')
        # user3 = User('Daniel', 'pw87465')
        # print(user1)
        # print(user2)
        # print(user3)
