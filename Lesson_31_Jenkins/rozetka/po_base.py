import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

EL_TIMEOUT = 15


class BasePageObject:

    @staticmethod
    def web_element(browser, location, clickable=False):
        try:
            if clickable:
                el = WebDriverWait(browser, EL_TIMEOUT).until(ec.element_to_be_clickable(location))
            else:
                el = WebDriverWait(browser, EL_TIMEOUT).until(ec.presence_of_element_located(location))
            return el
        except TimeoutException:
            pytest.fail(f'Element with {location=} did not found')

    @staticmethod
    def select_element_by_mouse(browser, element):
        try:
            actions = ActionChains(browser)
            actions.move_to_element(element).perform()
            return True
        except Exception as g_exc:
            pytest.fail(f'Unable to move mouse to defined element {g_exc}')
