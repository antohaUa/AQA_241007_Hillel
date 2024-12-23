import pytest
import time


@pytest.fixture(scope='module')
def some_code():
    # setup
    print('\nSleeping 2 sec...')
    time.sleep(2)
    yield 'SomeString'

    # teardown
    print('Teardown...')


@pytest.fixture(scope='module')
def alternative_code():
    # setup
    print('\nSleeping 3 sec...')
    time.sleep(2)
    yield 'SomeString'

    # teardown
    print('Teardown2...')
