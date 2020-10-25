import os
import pytest

from flix import create_app
from flix.adapters import memory_repository
from flix.adapters.memory_repository import MemoryRepository


TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'Jacky', 'Documents', 'COMPSCI235-GitHub', 'CS235Assignment2',
                              'tests', 'data')


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(TEST_DATA_PATH, repo)
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()