"""Some api testing class"""
import logging

import pytest
from pathlib import Path
from pytest_plugin import Cfg

from tests.test_blocks.tb_login import TestAuth
from tests.test_blocks.tb_media import TestMedia

CLEANUP = Cfg.cli_args.get('--cleanup', False)

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)


class TestAllApi(TestAuth, TestMedia):
    """Test cases for some APIs"""
    __test__ = True

    @pytest.fixture(scope='class', autouse=True)
    def cleanup(self):
        yield
        _log.info('-' * 10)
        _log.info('Post cleanup')
        if bool(CLEANUP):
            for curr_path in Path("").glob("test_*.png"):
                _log.debug(str(curr_path))
                curr_path.unlink()

    def test_smth(self):
        assert True
