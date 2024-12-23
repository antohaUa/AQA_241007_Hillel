import pytest
import time

t1 = (1, 2, 3, 4)


# class setup
#  class run    < --- class body

#  function setup
# function run     <--- test body
# function teardown

#  function setup
# function run    < --- test body
# function teardown

# function setup
# function run    <--- test body
# function teardown

# class teardown


# @pytest.mark.slow
# @pytest.mark.usefixtures('some_code')
class TestSomeTesting:

    @pytest.fixture(scope='class', autouse=True)
    def additional_print(self):
        # print('$' * 40)
        # yield
        # print('W' * 10)
        pass

    @pytest.fixture(scope='function')
    def some_code(self):
        # setup
        # raise ValueError()
        # print('Sleeping 5 sec...')
        # time.sleep(5)
        yield 'SomeString'

        # teardown
        print('Teardown...')

    def test_a_001(self):
        # conn = some_code
        # print(conn)
        print('Test start')
        assert 2 * 5 == 10, 'Something went wrong'

    def test_a_002(self):
        # some_result = some_code
        # print(some_result)
        print('*' * 40)
        print('Debug log')
        assert type(t1) == tuple
