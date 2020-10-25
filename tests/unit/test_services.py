import pytest

from flix.authentication.services import AuthenticationException
from flix.authentication import services as auth_services


def test_can_add_user(in_memory_repo):
    username = "sam"
    password = "abcD1234"

    auth_services.add_user(username, password, in_memory_repo)

    user_as_dict = auth_services.get_user(username, in_memory_repo)
    assert user_as_dict["username"] == username

    assert user_as_dict["password"].startswith('pbkdf2:sha256')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_valid_credentials(in_memory_repo):
    username = 'pmccartney'
    password = 'abcd1A23'

    auth_services.add_user(username, password, in_memory_repo)

    try:
        auth_services.authenticate_user(username, password, in_memory_repo)
    except AuthenticationException:
        assert False


def test_authentication_with_invalid_credentials(in_memory_repo):
    username = 'pmccartney'
    password = 'abcd1A23'

    auth_services.add_user(username, password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(username, 'abcd1A234', in_memory_repo)
