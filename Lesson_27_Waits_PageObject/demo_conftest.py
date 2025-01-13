"""Fixtures and setup code for the test suite."""
import pytest
from selenium import webdriver

BASE_URL = 'http://localhost:80/dz.html'

drivers = {
    'Chrome': webdriver.Chrome,
    'Firefox': webdriver.Firefox,
}


@pytest.fixture(params=drivers.keys(), scope='class')
def browser_driver(request):
    """Fixture to set up the browser driver.
    Args:
        request (Fixture): Pytest fixture used to get the current browser name.
    Yields:
        WebDriver: The initialized browser driver.
    """
    browser_name = request.param
    driver = drivers[browser_name]()
    driver.get(BASE_URL)

    yield driver

    driver.quit()
