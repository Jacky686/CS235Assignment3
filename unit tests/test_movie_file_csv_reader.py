import pytest

from datafilereaders.movie_file_csv_reader import MovieFileCSVReader


def test_external_rating():
    filename = "testfiles/Data1000Movies.csv"
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    assert len(movie_file_reader.dataset_of_movies) == 1000
    assert movie_file_reader.dataset_of_movies[9].external_rating == 7


def test_rating_votes():
    filename = "testfiles/Data1000Movies.csv"
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    assert len(movie_file_reader.dataset_of_movies) == 1000
    assert movie_file_reader.dataset_of_movies[12].rating_votes == 323118


def test_revenue_in_millions():
    filename = "testfiles/Data1000Movies.csv"
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    assert len(movie_file_reader.dataset_of_movies) == 1000
    assert movie_file_reader.dataset_of_movies[20].revenue_in_millions == 7.22


def test_metascore():
    filename = "testfiles/Data1000Movies.csv"
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    assert len(movie_file_reader.dataset_of_movies) == 1000
    assert movie_file_reader.dataset_of_movies[28].metascore == 60
