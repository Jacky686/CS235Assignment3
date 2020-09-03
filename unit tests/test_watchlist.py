import pytest

from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList


def test_init():
    watchlist1 = WatchList()
    assert watchlist1.watch_list == []
    assert watchlist1.size() == 0


def test_add_movie():
    watchlist2 = WatchList()
    watchlist2.add_movie(Movie("Moana", 2016))
    assert repr(watchlist2.watch_list[0]) == "<Movie Moana, 2016>"


def test_add_same_movie():
    watchlist3 = WatchList()
    watchlist3.add_movie(Movie("Moana", 2016))
    watchlist3.add_movie(Movie("Moana", 2016))
    assert repr(watchlist3.first_movie_in_watchlist()) == "<Movie Moana, 2016>"


def test_check_size():
    watchlist4 = WatchList()
    watchlist4.add_movie(Movie("Moana", 2016))
    watchlist4.add_movie(Movie("Ice Age", 2002))
    assert watchlist4.size() == 2


def test_remove_movie():
    watchlist5 = WatchList()
    watchlist5.add_movie(Movie("Moana", 2016))
    watchlist5.remove_movie(Movie("Transformers", 2007))
    assert watchlist5.size() == 1
    assert repr(watchlist5.first_movie_in_watchlist()) == "<Movie Moana, 2016>"


def test_add_and_remove_movie():
    watchlist6 = WatchList()
    watchlist6.add_movie(Movie("Moana", 2016))
    watchlist6.remove_movie(Movie("Moana", 2016))
    assert watchlist6.watch_list == []
    assert watchlist6.size() == 0


def test_select_movie():
    watchlist7 = WatchList()
    watchlist7.add_movie(Movie("Moana", 2016))
    watchlist7.add_movie(Movie("Transformers", 2007))
    watchlist7.add_movie(Movie("Ice Age", 2002))
    assert repr(watchlist7.select_movie_to_watch(2)) == "<Movie Ice Age, 2002>"


def test_select_movie_out_of_range():
    watchlist8 = WatchList()
    watchlist8.add_movie(Movie("Moana", 2016))
    watchlist8.add_movie(Movie("Transformers", 2007))
    watchlist8.add_movie(Movie("Ice Age", 2002))
    assert repr(watchlist8.select_movie_to_watch(3)) == "None"


def test_iter_and_next():
    watchlist9 = WatchList()
    watchlist9.add_movie(Movie("Moana", 2016))
    watchlist9.add_movie(Movie("Transformers", 2007))
    watchlist9.add_movie(Movie("Ice Age", 2002))
    watchlist_iter1 = iter(watchlist9)
    assert repr(next(watchlist_iter1)) == "<Movie Moana, 2016>"
    assert repr(next(watchlist_iter1)) == "<Movie Transformers, 2007>"
    assert repr(next(watchlist_iter1)) == "<Movie Ice Age, 2002>"


def test_next_out_of_range():
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
