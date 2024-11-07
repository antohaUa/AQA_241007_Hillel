import pytest


@pytest.mark.fast
def test_d_001():
    assert 12 > 3, 'Wrong statement'


@pytest.mark.fast
def test_d_002():
    assert True, 'Wrong statement'


@pytest.mark.xfail
def test_d_003():
    import time
    time.sleep(2)
    print("Something")
    assert False, 'Wrong statement'


def test_d_004():
    pytest.fail('Just fail')


def test_d_005():
    a = 1

