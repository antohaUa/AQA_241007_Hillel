import pytest
import logging

_log = logging.getLogger('Main')


@pytest.fixture(scope='module')
def decorator():
    print()
    _log.info(f"{'=' * 50}")
    yield
    _log.info('-' * 50)
