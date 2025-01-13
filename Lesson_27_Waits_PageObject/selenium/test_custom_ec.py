import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://127.0.0.1/custom_attribute.html'
ELEMENT_WAIT = 5


class CustomCondition:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)
            return element.is_displayed()  # True/False
        except Exception:
            return False

        # Setup WebDriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def test_custom_attribute(driver):
    # Find the input field and the button
    input_field = driver.find_element(By.ID, 'inputField')
    button = driver.find_element(By.TAG_NAME, 'button')

    # Input some text
    input_text = "TestValue"
    input_field.send_keys(input_text)

    # Click the button to trigger the attribute change
    button.click()

    # Wait for a moment to ensure the page updates
    driver.implicitly_wait(2)

    alert = driver.switch_to.alert
    alert.accept()

    # Wait for the element to have the 'custom' attribute set
    element = driver.find_element(By.ID, 'element')

    # driver.implicitly_wait(5)
    # time.sleep(5)
    # Assert the 'custom' attribute has been set correctly
    custom_attribute = element.get_attribute('custom')
    err_msg = f"Expected 'custom' attribute to be '{input_text}', but got '{custom_attribute}'"
    assert custom_attribute == input_text, err_msg

    # Custom condition:
    WebDriverWait(driver, ELEMENT_WAIT).until(
        lambda _: element.get_attribute('custom') == input_text
    )

    WebDriverWait(driver, ELEMENT_WAIT).until(CustomCondition((By.XPATH, f"//div[@custom='{input_text}']")))
