from sqlalchemy import (
    Table, MetaData, Column, Integer, Float, String, Text, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

from flix.domain import model

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)


directors = Table(
    'directors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('full_name', String(255), nullable=False),
    Column('movie_id', ForeignKey('movies.id'))
)

genres = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('movie_id', ForeignKey('movies.id'))
)

actors = Table(
    'actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('full_name', String(255), nullable=False),
    Column('movie_id', ForeignKey('movies.id'))
)

movies = Table(
    'movies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), unique=False, nullable=False),
    Column('release_year', Integer),
    Column('description', Text),
    Column('runtime_minutes', Integer),
    Column('external_rating', Float),
    Column('rating_votes', Integer),
    Column('revenue_in_millions', Float),
    Column('metascore', Integer)
)


def map_model_to_tables():
    mapper(model.User, users, properties={
        '_User__user_name': users.columns.username,
        '_User__password': users.columns.password,
    })
    mapper(model.Director, directors, properties={
        '_Director__director_full_name': directors.columns.full_name
    })
    mapper(model.Actor, actors, properties={
        '_Actor__actor_full_name': actors.columns.full_name
    })
    mapper(model.Genre, genres, properties={
        '_Genre__genre_name': genres.columns.name
    })
    mapper(model.Movie, movies, properties={
        '_Movie__title': movies.columns.title,
        '_Movie__release_year': movies.columns.release_year,
        '_Movie__description': movies.columns.description,
        '_Movie__runtime_minutes': movies.columns.runtime_minutes,
        '_Movie__director': relationship(model.Director, backref='_movie'),
        '_Movie__actors': relationship(model.Actor, backref='_movie'),
        '_Movie__genres': relationship(model.Genre, backref='_movie'),
        '_Movie__external_rating': movies.columns.external_rating,
        '_Movie__rating_votes': movies.columns.rating_votes,
        '_Movie__revenue_in_millions': movies.columns.revenue_in_millions,
        '_Movie__metascore': movies.columns.metascore
    })
