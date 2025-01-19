import time

import pytest
from selenium import webdriver

from po_smartphones import SmartphonesPage

PAGE_URL = '/mobile-phones/c80003'

SORTING_WAIT_TIMEOUT = 5
MIN_PRICE_DEFAULT = 999
MAX_PRICE = 20000


class TestSmartPhones:

    @pytest.fixture
    def driver(self):
        """Fixture for setting up and tearing down the WebDriver instance."""
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.fixture
    def smart_phones_po(self, driver):
        yield SmartphonesPage(driver=driver)

    @pytest.fixture(scope='class')
    def url(self, request):
        base_url = request.config.getoption("--baseurl")
        yield f'{base_url}{PAGE_URL}'

    def test_filter_smartphones(self, url, driver, smart_phones_po):
        smart_phones_po.load(url)

        # apple checkbox
        initial_url = driver.current_url
        apple_checkbox = smart_phones_po.brand_filter_checkbox(brand='Apple')
        apple_checkbox.click()
        assert smart_phones_po.check_page_reloaded(initial_url), 'There was no page URL reload'

        # samsung checkbox
        initial_url = driver.current_url
        samsung_checkbox = smart_phones_po.brand_filter_checkbox(brand='Samsung')
        samsung_checkbox.click()
        assert smart_phones_po.check_page_reloaded(initial_url), 'There was no page URL reload'

        # sorting and price
        smart_phones_po.select_sorting_type('Від дорогих до дешевих')
        time.sleep(SORTING_WAIT_TIMEOUT)
        initial_url = driver.current_url
        smart_phones_po.set_max_price(max_price=MAX_PRICE)
        smart_phones_po.confirm_price_filter()
        assert smart_phones_po.check_page_reloaded(initial_url), 'There was no page URL reload'

        # check prices range
        prices = smart_phones_po.phone_prices()
        err_msg = 'Found price that not match filter'
        assert all(MIN_PRICE_DEFAULT < int(itm.text.strip('₴').replace(' ', '')) < MAX_PRICE for itm in prices), err_msg
        print('All prices within defined price range')
