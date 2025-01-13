import pytest
from selenium import webdriver

from po_auth_demo import AuthPage

DRIVER_LOAD_TIME = 2


class TestAuthPage:

    @pytest.fixture
    def driver(self):
        """Fixture for setting up and tearing down the WebDriver instance."""
        driver = webdriver.Chrome()
        driver.implicitly_wait(DRIVER_LOAD_TIME)
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        """Test case for a successful login."""
        auth_page = AuthPage(driver)
        auth_page.load()

        auth_page.set_username("testuser")
        auth_page.set_password("testpassword")
        auth_page.click_login()

        # check login alert present
        auth_page.check_login_alert(driver)

        # Assert no error message is displayed
        assert auth_page.get_error_message() is None

    def test_failed_login(self, driver):
        """Test case for a failed login."""
        auth_page = AuthPage(driver)
        auth_page.load()

        auth_page.set_username("wronguser")
        auth_page.set_password("wrongpassword")
        auth_page.click_login()

        # Assert error message is displayed
        error_message = auth_page.get_error_message()
        assert error_message == "Invalid username or password!", "Error message not displayed or incorrect."
