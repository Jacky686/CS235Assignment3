from typing import List, Iterable
from datetime import datetime


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True

        return False

    def __lt__(self, other):
        if self.__director_full_name < other.__director_full_name:
            return True

        return False

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other.__genre_name:
            return True

        return False

    def __lt__(self, other):
        if self.__genre_name < other.__genre_name:
            return True

        return False

    def __hash__(self):
        return hash(self.__genre_name)


class Actor:

    def __init__(self, actor_full_name: str, actor_colleagues=None):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        if actor_colleagues is None:
            self.__actor_colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, full_name: str):
        if isinstance(full_name, str):
            self.__actor_full_name = full_name.strip()

    @property
    def actor_colleagues(self):
        return self.__actor_colleagues

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.actor_full_name:
            return True

        return False

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True

        return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__actor_colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__actor_colleagues:
            return True

        return False


class Movie:

    def __init__(self, title: str, release_year: int):
        self.__title = title

        if type(release_year) is int and release_year >= 1900:
            self.__release_year = release_year
        else:
            self.__release_year = None

        self.__description: str = ""
        self.__director: List[Director] = list()
        self.__actors: List[Actor] = list()
        self.__genres: List[Genre] = list()
        self.__runtime_minutes: int = 0

        self.__external_rating: float = None
        self.__rating_votes: int = None
        self.__revenue_in_millions: float = None
        self.__metascore: int = None

        self.__reviews: List[Review] = list()

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
    def director(self) -> List[Director]:
        return self.__director

    @director.setter
    def director(self, director: List):
        if not any(not isinstance(director, Director) for d in director):
            self.__director = director

    def add_director(self, director: "Director"):
        if isinstance(director, Director):
            self.__director.append(director)

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

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews):
        if not any(not isinstance(review, Review) for review in reviews):
            self.__genres = reviews

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
    def reviews(self) -> List:
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


class Review:

    def __init__(self, user: User, movie: Movie, review_text: str, rating: int):
        self.__user = user

        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text

        if 1 <= rating <= 10 and type(rating) == int:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.now()

    @property
    def user(self) -> User:
        return self.__user

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> str:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}>"

    def __eq__(self, other):
        if self.__movie == other.movie and \
                self.__review_text == other.review_text and \
                self.__rating == other.rating and \
                self.__timestamp == other.__timestamp:
            return True

        return False


class WatchList:

    def __init__(self):
        self.__watch_list: List[Movie] = list()

    @property
    def watch_list(self) -> List[Movie]:
        return self.__watch_list

    def add_movie(self, movie):
        if isinstance(movie, Movie) and movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if isinstance(movie, Movie) and movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if 0 <= index < len(self.__watch_list):
            return self.__watch_list[index]
        else:
            return None

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if self.__watch_list:
            return self.__watch_list[0]
        else:
            return None

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.size():
            temp_i = self.i
            self.i += 1
            return self.__watch_list[temp_i]
        else:
            raise StopIteration
