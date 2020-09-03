import csv

from typing import List

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


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
                movie.director = director
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

                self.__dataset_of_movies.append(movie)
                # title = row['Title']
                # release_year = int(row['Year'])
                # print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1


class TestMovieFileCSVReader:

    def test_init(self):
        pass
        # filename = 'test.csv'
        # movie_file_reader = MovieFileCSVReader(filename)
        # movie_file_reader.read_csv_file()
        #
        # print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
        # print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
        # print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
        # print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
