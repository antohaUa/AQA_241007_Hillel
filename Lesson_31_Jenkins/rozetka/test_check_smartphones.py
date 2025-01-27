import time

import pytest
import allure
from selenium import webdriver

from po_smartphones import SmartphonesPage

PAGE_URL = '/mobile-phones/c80003'

SORTING_WAIT_TIMEOUT = 5
MIN_PRICE_DEFAULT = 999
MAX_PRICE = 20000


class TestSmartPhones:

    @pytest.fixture(scope='class')
    def driver(self):
        """Fixture for setting up and tearing down the WebDriver instance."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        # driver.maximize_window()
        print(driver.get_window_size())
        yield driver
        driver.quit()

    @pytest.fixture(scope='class')
    def smart_phones_po(self, driver):
        yield SmartphonesPage(driver=driver)

    @pytest.fixture(scope='class')
    def url(self, request):
        base_url = request.config.getoption("--baseurl")
        yield f'{base_url}{PAGE_URL}'

    @allure.feature('Filtering')
    def test_filter_smartphones(self, url, driver, smart_phones_po):
        smart_phones_po.load(url)

        print('Starting TC Aplle filtering')
        # apple checkbox
        initial_url = driver.current_url
        apple_checkbox = smart_phones_po.brand_filter_checkbox(brand='Apple')
        apple_checkbox.click()
        print('Button click')
        assert smart_phones_po.check_page_reloaded(initial_url), 'There was no page URL reload'

        print('Starting TC Samsung filtering')
        # samsung checkbox
        initial_url = driver.current_url
        samsung_checkbox = smart_phones_po.brand_filter_checkbox(brand='Samsung')
        samsung_checkbox.click()
        print('Button click')
        assert smart_phones_po.check_page_reloaded(initial_url), 'There was no page URL reload'

    @allure.feature('Sorting')
    def test_sorting_smartphones(self, url, driver, smart_phones_po):
        print('Sorting phase ...')
        # sorting and price
        smart_phones_po.select_sorting_type('Від дорогих до дешевих')
        time.sleep(SORTING_WAIT_TIMEOUT)
        smart_phones_po.set_max_price(max_price=MAX_PRICE)
        driver.save_screenshot('sorting.png')
        smart_phones_po.confirm_price_filter()

    @allure.feature('Pricing')
    def test_price_smartphones(self, url, driver, smart_phones_po):
        print('Checking price ...')
        # check prices range
        prices = smart_phones_po.phone_prices()
        err_msg = 'Found price that not match filter'
        assert all(MIN_PRICE_DEFAULT < int(itm.text.strip('₴').replace(' ', '')) < 10000 for itm in prices), err_msg
        print('All prices within defined price range')
