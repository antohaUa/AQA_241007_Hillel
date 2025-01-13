import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

URL = 'http://127.0.0.1/auth_err_handling.html'
BROWSERS = ("chrome", "firefox")


class TestAuthPageErr:
    # Pytest fixture for setting up the WebDriver
    # https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest.hookspec.pytest_generate_tests
    def pytest_generate_tests(self, metafunc):
        if "browser" in metafunc.fixturenames:
            metafunc.parametrize("browser", BROWSERS, indirect=True)

    @pytest.fixture
    def browser(self, request):
        browser_name = request.param
        # driver = getattr(webdriver, browser_name.capitalize())

        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.maximize_window()
        yield driver
        driver.quit()

    @staticmethod
    def webelement(browser, location):
        try:
            element = WebDriverWait(browser, 5).until(EC.presence_of_element_located(location))
            return element
        except TimeoutException:
            pytest.fail(f" Element with {location=} did not found.")

    @staticmethod
    def webelement_absent(browser, location):
        try:
            WebDriverWait(browser, 5).until_not(EC.presence_of_element_located(location))
            return True
        except TimeoutException:
            pytest.fail(f" Element with {location=} still on the page.")

    @staticmethod
    def check_message(browser, message_el, assert_text):
        try:
            message_element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(message_el))
            assert message_element.is_displayed(), assert_text
        except TimeoutException:
            pytest.fail("Expected message did not appear.")

    def test_login_page(self, browser):
        try:
            # Load the HTML page
            browser.get(URL)

            # Define element locators
            username_field = self.webelement(browser, (By.ID, "username"))
            absent_username_field = self.webelement_absent(browser, (By.ID, "username2"))
            # absent_username_field3 = browser.find_element(By.ID, "username3")
            password_field = (By.ID, "password")
            login_button = (By.ID, "loginButton")
            error_message = (By.ID, "errorMessage")
            success_message = (By.ID, "successMessage")

            # Interact with elements
            username_field.send_keys("wronguser")
            WebDriverWait(browser, 5).until(EC.presence_of_element_located(password_field)).send_keys("wrongpassword")
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable(login_button)).click()

            self.check_message(browser, error_message, "Error message not displayed for invalid credentials.")

            # Clear fields and enter valid credentials
            username_field.clear()
            browser.find_element(*password_field).clear()
            username_field.send_keys("testuser")
            browser.find_element(*password_field).send_keys("testpassword")
            browser.find_element(*login_button).click()

            self.check_message(browser, success_message, "Success message not displayed for valid credentials.")

        except NoSuchElementException:
            pytest.fail("Element not found. Stopping test...")
        except WebDriverException as e:
            pytest.fail(f"WebDriverException occurred: {e}")
        except Exception as e:
            pytest.fail(f"An unexpected exception occurred: {e}")
