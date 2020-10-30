from datetime import datetime

from flix.domain.model import Director, Genre, Actor, Movie, User, Review, WatchList

import pytest


@pytest.fixture()
def director():
    return Director("Chris Wedge")


@pytest.fixture()
def director2():
    return Director("Michael Bay")


@pytest.fixture()
def genre():
    return Genre("Horror")


@pytest.fixture()
def genre2():
    return Genre("Thriller")


@pytest.fixture()
def actor():
    return Actor("Jack Black")


@pytest.fixture()
def actor2():
    return Actor("Matt Damon")


@pytest.fixture()
def movie():
    return Movie("Ice Age", 2002)


@pytest.fixture()
def movie2():
    return Movie("Jason Bourne", 2016)


@pytest.fixture()
def user():
    return User("Bob12", "password888")


@pytest.fixture()
def user2():
    return User("Bob20", "password999")


@pytest.fixture()
def review():
    return Review(User("Bob12", "password888"), Movie("Ice Age", 2002), "Great", 8)


@pytest.fixture()
def watch_list():
    return WatchList()


def test_director_construction(director, director2):
    assert director.director_full_name == "Chris Wedge"
    assert repr(director) == "<Director Chris Wedge>"

    assert (director < director2) is True
    assert (director == director) is True


def test_genre_construction(genre, genre2):
    assert genre.genre_name == "Horror"
    assert repr(genre) == "<Genre Horror>"

    assert (genre < genre2) is True
    assert (genre == genre)


def test_actor_construction(actor, actor2):
    assert actor.actor_full_name == "Jack Black"
    assert repr(actor) == "<Actor Jack Black>"

    for actor in actor.actor_colleagues:
        assert False

    assert (actor < actor2) is True
    assert (actor == actor) is True


def test_movie_construction(movie, movie2):
    assert movie.title == "Ice Age"
    assert movie.release_year == 2002
    assert movie.description == ""
    assert movie.director == []

    for actor in movie.actors:
        assert False

    for genre in movie.genres:
        assert False

    assert movie.runtime_minutes == 0
    assert movie.external_rating is None
    assert movie.revenue_in_millions is None
    assert movie.metascore is None

    for review in movie.reviews:
        assert False

    assert repr(movie) == "<Movie Ice Age, 2002>"
    assert (movie < movie2) is True
    assert (movie == movie) is True


def test_user_construction(user, user2):
    assert user.user_name == "bob12"
    assert user.password == "password888"
    assert repr(user) == "<User bob12>"

    for movie in user.watched_movies:
        assert False

    for reivew in user.reviews:
        assert False

    assert user.time_spent_watching_movies_minutes == 0

    assert (user < user2) is True
    assert (user == user) is True


def test_review_construction(review, user, movie):
    assert review.user == user
    assert review.movie == movie
    assert review.review_text == "Great"
    assert review.rating == 8


#   Test WatchList
def test_watch_list_init():
    watchlist1 = WatchList()
    assert watchlist1.watch_list == []
    assert watchlist1.size() == 0


def test_watch_list_add_movie():
    watchlist2 = WatchList()
    watchlist2.add_movie(Movie("Moana", 2016))
    assert repr(watchlist2.watch_list[0]) == "<Movie Moana, 2016>"


def test_watch_list_add_same_movie():
    watchlist3 = WatchList()
    watchlist3.add_movie(Movie("Moana", 2016))
    watchlist3.add_movie(Movie("Moana", 2016))
    assert repr(watchlist3.first_movie_in_watchlist()) == "<Movie Moana, 2016>"


def test_watch_list_check_size():
    watchlist4 = WatchList()
    watchlist4.add_movie(Movie("Moana", 2016))
    watchlist4.add_movie(Movie("Ice Age", 2002))
    assert watchlist4.size() == 2


def test_watch_list_remove_movie():
    watchlist5 = WatchList()
    watchlist5.add_movie(Movie("Moana", 2016))
    watchlist5.remove_movie(Movie("Transformers", 2007))
    assert watchlist5.size() == 1
    assert repr(watchlist5.first_movie_in_watchlist()) == "<Movie Moana, 2016>"


def test_watch_list_add_and_remove_movie():
    watchlist6 = WatchList()
    watchlist6.add_movie(Movie("Moana", 2016))
    watchlist6.remove_movie(Movie("Moana", 2016))
    assert watchlist6.watch_list == []
    assert watchlist6.size() == 0


def test_watch_list_select_movie():
    watchlist7 = WatchList()
    watchlist7.add_movie(Movie("Moana", 2016))
    watchlist7.add_movie(Movie("Transformers", 2007))
    watchlist7.add_movie(Movie("Ice Age", 2002))
    assert repr(watchlist7.select_movie_to_watch(2)) == "<Movie Ice Age, 2002>"


def test_watch_list_select_movie_out_of_range():
    watchlist8 = WatchList()
    watchlist8.add_movie(Movie("Moana", 2016))
    watchlist8.add_movie(Movie("Transformers", 2007))
    watchlist8.add_movie(Movie("Ice Age", 2002))
    assert repr(watchlist8.select_movie_to_watch(3)) == "None"


def test_watch_list_iter_and_next():
    watchlist9 = WatchList()
    watchlist9.add_movie(Movie("Moana", 2016))
    watchlist9.add_movie(Movie("Transformers", 2007))
    watchlist9.add_movie(Movie("Ice Age", 2002))
    watchlist_iter1 = iter(watchlist9)
    assert repr(next(watchlist_iter1)) == "<Movie Moana, 2016>"
    assert repr(next(watchlist_iter1)) == "<Movie Transformers, 2007>"
    assert repr(next(watchlist_iter1)) == "<Movie Ice Age, 2002>"


def test_watch_list_next_out_of_range():
    watchlist10 = WatchList()
    watchlist10.add_movie(Movie("Moana", 2016))
    watchlist10.add_movie(Movie("Transformers", 2007))
    watchlist10.add_movie(Movie("Ice Age", 2002))
    watchlist_iter2 = iter(watchlist10)
    assert repr(next(watchlist_iter2)) == "<Movie Moana, 2016>"
    assert repr(next(watchlist_iter2)) == "<Movie Transformers, 2007>"
    assert repr(next(watchlist_iter2)) == "<Movie Ice Age, 2002>"
    with pytest.raises(StopIteration):
        print(next(watchlist_iter2))