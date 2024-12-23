import pytest
import time

t1 = (1, 2, 3, 4)


# class setup
#  class run
#  function setup
# function run
# function teardown


# function setup
# function run         <----------------
# function teardown

# function setup
# function run        <-------------------
# function teardown

# class teardown
@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    # setup
    print('\nHello Module World...')
    yield 'Connection'
    # teardown
    print('\nBye Module World...')


@pytest.mark.slow
@pytest.mark.usefixtures('alternative_code', 'some_code')
class TestSomeTesting2:

    # @pytest.fixture(scope='function', autouse=True)
    # def some_code(self):
    #     # setup
    #     print('Sleeping 5 sec...')
    #     time.sleep(5)
    #     yield 'SomeString'
    #
    #     # teardown
    #     print('Teardown...')

    @pytest.fixture(scope='function')
    def function_fixture(self):
        # setup
        print('\nHello World...')
        yield 'Connection'
        # teardown
        print('\nBye World...')

    def test_a_003(self):
        # print('Test start')
        assert 2 * 5 == 10, 'Something went wrong'

    def test_a_004(self, function_fixture):
        # some_result = some_code
        # print(some_result)
        ##print('*' * 40)
        # print('Debug log')
        print(function_fixture)
        assert type(t1) == tuple
