import logging

_log = logging.getLogger('Main')

import requests
from requests.auth import HTTPBasicAuth
from pytest_plugin import Cfg

USR = Cfg.params.get('usr')
PWD = Cfg.params.get('pwd')
API_BASE_URL = Cfg.params.get('api_base_url')


class TestAuth:
    __test__ = False

    def test_positive_auth(self):
        basic = HTTPBasicAuth(USR, PWD)
        breakpoint()
        response = requests.get(f'{API_BASE_URL}/basic-auth/user/pass', auth=basic)
        assert response.status_code == 200, f'Incorrect response code {response.status_code}'
        assert response.json().get('authenticated') is True, 'Auth failed'
        _log.debug(response.text)

    def test_negative_auth(self):
        basic = HTTPBasicAuth(USR, 'wrong_pass')
        response = requests.get(f'{API_BASE_URL}/basic-auth/user/pass', auth=basic)
        assert response.status_code == 401, f'Incorrect response code {response.status_code}'
