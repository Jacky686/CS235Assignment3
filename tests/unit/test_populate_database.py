from sqlalchemy import select, inspect

from flix.adapters.orm import metadata


def test_database_populate_inspect_table_names(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == ['actors', 'directors', 'genres', 'movies', 'users']


def test_database_populate_select_all_users(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_users_table = inspector.get_table_names()[4]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_users_table]])
        result = connection.execute(select_statement)

        all_users = []
        for row in result:
            all_users.append(row['username'])

        assert all_users == ['thorke', 'fmercury', 'mjackson']


def test_database_populate_select_all_movies(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_movies_table = inspector.get_table_names()[3]

    with database_engine.connect() as connection:
        # query for records in table movies
        select_statement = select([metadata.tables[name_of_movies_table]])
        result = connection.execute(select_statement)

        all_movies = []
        for row in result:
            all_movies.append((row['title'], row['release_year'], row['description'], row['runtime_minutes'],
                               row['external_rating'], row['rating_votes'], row['revenue_in_millions'],
                               row['metascore']))

            assert all_movies[0] == ('Guardians of the Galaxy', 2014,
                                     'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.',
                                     121, 8.1, 757074, 333.13, 76)

            assert all_movies[99] == ('The Departed', 2006,
                                                 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',
                                                 151, 8.5, 937414, 132.37, 85)


def test_database_populate_select_all_genres(database_engine):
    inspector = inspect(database_engine)
    name_of_genres_table = inspector.get_table_names()[2]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_genres_table]])
        result = connection.execute(select_statement)

        all_genres = []
        for row in result:
            all_genres.append((row['name'], row['movid_id']))

            assert all_genres[0] == ('Action', 1)
            assert all_genres[50] == ('Thriller', 18)


def test_database_populate_select_all_directors(database_engine):
    inspector = inspect(database_engine)
    name_of_directors_table = inspector.get_table_names()[1]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_directors_table]])
        result = connection.execute(select_statement)

        all_directors = []
        for row in result:
            all_directors.append((row['full_name'], row['movid_id']))

            assert all_directors[0] == ('James Gunn', 1)
            assert all_directors[80] == ('Paul Feig', 80)


def test_database_populate_select_all_actors(database_engine):
    inspector = inspect(database_engine)
    name_of_actors_table = inspector.get_table_names()[0]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_actors_table]])
        result = connection.execute(select_statement)

        all_actors = []
        for row in result:
            all_actors.append((row['full_name'], row['movid_id']))

            assert all_actors[0] == ('Chris Pratt', 1)
            assert all_actors[100] == ('Maika Monroe', 25)