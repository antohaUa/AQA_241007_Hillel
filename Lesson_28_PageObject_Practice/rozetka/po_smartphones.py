import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

ELEMENT_WAIT_TIMEOUT = 15
DRIVER_LOAD_TIME = 10


class SmartphonesPage:

    def __init__(self, driver):
        self.driver = driver

    def get_brand_filter_element(self, brand):
        try:
            el_filter = (By.XPATH, f'//rz-indexed-link[@data-id="{brand}"]/a')
            element = WebDriverWait(self.driver, ELEMENT_WAIT_TIMEOUT).until(EC.element_to_be_clickable(el_filter))
            return element
        except TimeoutException:
            pytest.fail(f" Brand filter '{brand}' not found.")

    def load(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(DRIVER_LOAD_TIME)

    # def set_username(self, username):
    #     self.driver.find_element(*self.username_input).clear()
    #     self.driver.find_element(*self.username_input).send_keys(username)
    #
    # def set_password(self, password):
    #     self.driver.find_element(*self.password_input).clear()
    #     self.driver.find_element(*self.password_input).send_keys(password)
    #
    # def click_login(self):
    #     self.driver.find_element(*self.login_button).click()
    #
    # @staticmethod
    # def check_login_alert(driver):
    #     # Check if an alert is displayed
    #     WebDriverWait(driver, ELEMENT_WAIT_TIMEOUT).until(EC.alert_is_present())
    #     alert = driver.switch_to.alert
    #     assert alert.text == "Login successful!"
    #     alert.accept()
    #     print('Login alert detected')
    #
    # def get_error_message(self):
    #     try:
    #         error_element = WebDriverWait(self.driver, ELEMENT_WAIT_TIMEOUT).until(
    #             EC.visibility_of_element_located(self.error_message)
    #         )
    #         return error_element.text
    #     except Exception as g_exc:
    #         print(g_exc)
    #         return None
