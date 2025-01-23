import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait

from po_base import BasePageObject

DRIVER_LOAD_TIME = 10
PAGE_RELOAD_TIMEOUT = 10
ELEMENT_WAIT_TIMEOUT = 15
ELEMENTS_LOAD_TIME = 5


class SmartphonesPage(BasePageObject):

    def __init__(self, driver):
        """Init."""
        self.driver = driver

    def brand_filter_checkbox(self, brand):
        el_filter = (By.XPATH, f'//rz-indexed-link[@data-id="{brand}"]')
        element = self.web_element(self.driver, el_filter)
        self.select_element_by_mouse(self.driver, element)
        checkbox_filter = (By.XPATH, f'//rz-indexed-link[@data-id="{brand}"]/a')
        checkbox = self.web_element(self.driver, checkbox_filter, clickable=True)
        return checkbox

    def load(self, url):
        try:
            self.driver.get(url)
            # Wait for the document to be fully loaded
            WebDriverWait(self.driver, DRIVER_LOAD_TIME).until(
                lambda d: d.execute_script('return document.readyState') == 'complete',
            )
            # check one of the element that loaded in last group
            last_xpath = '//div[@class="rz-banner__title"]'
            self.web_element(self.driver, (By.XPATH, last_xpath))
            return True
        except TimeoutException:
            pytest.fail('Unable to load page')

    def check_page_reloaded(self, prev_url):
        try:
            WebDriverWait(self.driver, PAGE_RELOAD_TIMEOUT).until(lambda d: d.current_url != prev_url)
            return True
        except TimeoutException:
            return False

    def select_sorting_type(self, sorting_type):
        xpath_select = '//rz-sort/select'
        select_element = self.web_element(self.driver, (By.XPATH, xpath_select))
        dropdown = Select(select_element)
        dropdown.select_by_visible_text(sorting_type)

    def set_max_price(self, max_price):
        price_max = (By.XPATH, '//input[@formcontrolname="max"]')
        price_max_input = self.web_element(self.driver, price_max)
        price_max_input.clear()
        price_max_input.send_keys(max_price)

    def confirm_price_filter(self):
        price_button = (By.XPATH, '//fieldset/div/button[@type="submit"]')
        price_button_element = self.web_element(self.driver, price_button, clickable=True)
        price_button_element.click()

    def phone_prices(self):
        self.driver.implicitly_wait(ELEMENTS_LOAD_TIME)
        return self.driver.find_elements(By.XPATH, '//span[@class="goods-tile__price-value"]')
