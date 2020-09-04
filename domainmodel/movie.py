from typing import List, Iterable

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:

    def __init__(self, title: str, release_year: int):
        self.__title = title

        if type(release_year) is int and release_year >= 1900:
            self.__release_year = release_year
        else:
            self.__release_year = None

        self.__description: str = ""
        self.__director: Director = None
        self.__actors: List[Actor] = list()
        self.__genres: List[Genre] = list()
        self.__runtime_minutes: int = 0

        self.__external_rating: float = None
        self.__rating_votes: int = None
        self.__revenue_in_millions: float = None
        self.__metascore: int = None

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if title == "" or type(title) is not str:
            self.__title = ""
        else:
            self.__title = title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if isinstance(description, str):
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if isinstance(director, Director) and self.__director is None:
            self.__director = director

    @property
    def actors(self) -> Iterable["Actor"]:
        return self.__actors

    @actors.setter
    def actors(self, actors: List):
        if not any(not isinstance(actor, Actor) for actor in actors):
            self.__actors = actors

    @property
    def genres(self) -> Iterable["Genre"]:
        return self.__genres

    @genres.setter
    def genres(self, genres: List):
        if not any(not isinstance(genre, Genre) for genre in genres):
            self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes: int):
        if isinstance(runtime_minutes, int) and runtime_minutes > 0:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError

    @property
    def external_rating(self) -> float:
        return self.__external_rating

    @external_rating.setter
    def external_rating(self, external_rating: float):
        if isinstance(external_rating, float) and 0 <= external_rating <= 10:
            self.__external_rating = external_rating

    @property
    def rating_votes(self):
        return self.__rating_votes

    @rating_votes.setter
    def rating_votes(self, rating_votes):
        if isinstance(rating_votes, int) and rating_votes >= 0:
            self.__rating_votes = rating_votes

    @property
    def revenue_in_millions(self):
        return self.__revenue_in_millions

    @revenue_in_millions.setter
    def revenue_in_millions(self, revenue_in_millions):
        if isinstance(revenue_in_millions, float) and revenue_in_millions > 0:
            self.__revenue_in_millions = revenue_in_millions

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, metascore):
        if isinstance(metascore, int) and metascore > 0:
            self.__metascore = metascore

    def add_actor(self, actor: "Actor"):
        if isinstance(actor, Actor):
            self.__actors.append(actor)

    def remove_actor(self, actor: "Actor"):
        if isinstance(actor, Actor):
            try:
                self.__actors.remove(actor)
            except ValueError:
                pass

    def add_genre(self, genre: "Genre"):
        if isinstance(genre, Genre):
            self.__genres.append(genre)

    def remove_genre(self, genre: "Genre"):
        if isinstance(genre, Genre):
            try:
                self.__genres.remove(genre)
            except ValueError:
                pass

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if self.__title == other.__title and self.__release_year == other.__release_year:
            return True

        return False

    def __lt__(self, other):
        if self.__title + str(self.__release_year) < other.__title + str(other.__release_year):
            return True

        return False

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))


class TestMovieMethods:

    def test_init(self):
        pass
        # movie = Movie("Moana", 2016)
        # print(movie)
        #
        # director = Director("Ron Clements")
        # movie.director = director
        # print(movie.director)
        #
        # actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        # for actor in actors:
        #     movie.add_actor(actor)
        # print(movie.actors)
        #
        # movie.runtime_minutes = 107
        # print("Movie runtime: {} minutes".format(movie.runtime_minutes))
