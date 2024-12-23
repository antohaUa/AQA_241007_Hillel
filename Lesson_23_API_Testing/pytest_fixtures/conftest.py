import pytest
import time


@pytest.fixture(scope='module')
def some_code():
    # setup
    print('Sleeping 1 sec...')
    time.sleep(1)
    yield 'SomeString'

    # teardown
    print('Teardown...')
