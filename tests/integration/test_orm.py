import pytest

from sqlalchemy.exc import IntegrityError
from flix.domain.model import Director, Genre, Actor, Movie, User, Review, WatchList


def insert_user(empty_session, values=None):
    new_name = "Andrew"
    new_password = "1234"

    if values is not None:
        new_name = values[0]
        new_password = values[1]

    empty_session.execute('INSERT INTO users (username, password) VALUES (:username, :password)',
                          {'username': new_name, 'password': new_password})
    row = empty_session.execute('SELECT id from users where username = :username',
                                {'username': new_name}).fetchone()
    return row[0]


def insert_users(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO users (username, password) VALUES (:username, :password)',
                              {'username': value[0], 'password': value[1]})
    rows = list(empty_session.execute('SELECT id from users'))
    keys = tuple(row[0] for row in rows)
    return keys


def make_user():
    user = User("Andrew", "111")
    return user


def insert_movie(empty_session, values=None):
    new_title = "Ice Age"
    new_release_year = 2002
    new_description = "The ice age"
    new_runtime_minutes = 120
    new_external_rating = 8.5
    new_rating_votes = 5000
    new_revenue_in_millions = 100
    new_metascore = 88

    if values is not None:
        new_title = values[0]
        new_release_year = values[1]
        new_description = values[2]
        new_runtime_minutes = values[3]
        new_external_rating = values[4]
        new_rating_votes = values[5]
        new_revenue_in_millions = values[6]
        new_metascore = values[7]

    empty_session.execute(
        'INSERT INTO movies (title, release_year, description, runtime_minutes, external_rating, rating_votes, revenue_in_millions, metascore) VALUES (:title, :release_year, :description, :runtime_minutes, :external_rating, :rating_votes, :revenue_in_millions, :metascore)',
        {'title': new_title, 'release_year': new_release_year, 'description': new_description,
         'runtime_minutes': new_runtime_minutes, 'external_rating': new_external_rating,
         'rating_votes': new_rating_votes, 'revenue_in_millions': new_revenue_in_millions, 'metascore': new_metascore})
    row = empty_session.execute('SELECT id from movies where title = :title',
                                {'title': new_title}).fetchone()
    return row[0]


def make_movie():
    movie = Movie("Ice Age", 2002)
    return movie


def test_loading_of_users(empty_session):
    users = list()
    users.append(("andrew", "1234"))
    users.append(("cindy", "1111"))
    insert_users(empty_session, users)

    expected = [
        User("Andrew", "1234"),
        User("Cindy", "999")
    ]
    assert empty_session.query(User).all() == expected


def test_saving_of_users(empty_session):
    user = make_user()
    empty_session.add(user)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT username, password FROM users'))
    assert rows == [("andrew", "111")]


def test_saving_of_movies(empty_session):
    movie = make_movie()
    empty_session.add(movie)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT title, release_year FROM movies'))
    assert rows == [("Ice Age", 2002)]