from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://localhost:80/auth_demo.html'
ELEMENT_WAIT_TIMEOUT = 3


class AuthPage:
    """
    Page Object Model for the Authentication Page
    """

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, ".btn")
        self.error_message = (By.ID, "errorMessage")

    def load(self):
        self.driver.get(URL)

    def set_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    @staticmethod
    def check_login_alert(driver):
        # Check if an alert is displayed
        WebDriverWait(driver, ELEMENT_WAIT_TIMEOUT).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "Login successful!"
        alert.accept()
        print('Login alert detected')

    def get_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, ELEMENT_WAIT_TIMEOUT).until(
                EC.visibility_of_element_located(self.error_message)
            )
            return error_element.text
        except Exception as g_exc:
            print(g_exc)
            return None
