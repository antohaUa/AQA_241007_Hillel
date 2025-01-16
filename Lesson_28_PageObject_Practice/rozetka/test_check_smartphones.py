import pytest
import time
from selenium import webdriver

from po_smartphones import SmartphonesPage

BASE_URL = 'https://rozetka.com.ua'
PAGE_URL = '/mobile-phones/c80003'
URL = f'{BASE_URL}{PAGE_URL}'


class TestSmartPhones:

    @pytest.fixture
    def driver(self):
        """Fixture for setting up and tearing down the WebDriver instance."""
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_filter_smartphones(self, driver):
        smart_phones_po = SmartphonesPage(driver=driver)
        smart_phones_po.load(URL)
        time.sleep(10)
        apple_filter = smart_phones_po.get_brand_filter_element(brand='Apple')
        apple_filter.click()
        #driver.refresh()
        smart_phones_po.load(f'{URL}/producer=apple/')
        time.sleep(10)
        # with open('content.html', 'wt') as cont_fh:
        #     content = driver.page_source
        #     cont_fh.write(content)
        breakpoint()
        samsung_filter = smart_phones_po.get_brand_filter_element(brand='Samsung')
        samsung_filter.click()
        time.sleep(5)
        smart_phones_po.load(f'{URL}/producer=apple,samsung/')
        time.sleep(5)
