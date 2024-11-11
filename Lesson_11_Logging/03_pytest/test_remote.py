import pytest
import requests

base_url = 'http://127.0.0.1:8080'
auth = {'username': 'admin', 'password': 'adminpassword'}
wrong_auth = {'username': 'admin', 'password': 'bad_password'}


@pytest.mark.login
def test_passed_login():
    response = requests.post(f'{base_url}/login', json=auth)
    assert response.status_code == 200, "Unsuccessful login"
    assert response.json().get('message') == "Logged in successfully!"


@pytest.mark.login
def test_wrong_login():
    response = requests.post(f'{base_url}/login', json=wrong_auth)
    assert response.status_code == 401, "Not expected code"
    assert response.json().get('message') == "Invalid credentials!"


def test_fake():
    assert True
