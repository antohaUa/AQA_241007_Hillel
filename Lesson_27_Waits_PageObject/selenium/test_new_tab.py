import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

URL = 'http://127.0.0.1/new_tab.html'

# Setup WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def test_open_new_tab_and_alert(driver):
    window_handles_prev = driver.window_handles
    print(window_handles_prev)

    # Find the button and click it to open a new tab
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    # Wait for the new tab to open
    time.sleep(1)

    # Get the handles of all open windows/tabs
    window_handles = driver.window_handles
    print(window_handles)

    # Switch to the new tab
    driver.switch_to.window(window_handles[-1])

    # Verify the content in the new tab
    new_tab_title = driver.title
    assert new_tab_title == 'New Tab', f"Expected title to be 'New Tab', but got {new_tab_title}"

    # Click the button in the new tab
    new_tab_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    new_tab_button.click()

    # Wait for the alert to appear
    time.sleep(1)

    # Handle the alert and verify its message
    alert = Alert(driver)
    alert_message = alert.text
    assert alert_message == 'You clicked the button!', f"Expected alert message 'You clicked the button!', but got {alert_message}"

    # Accept the alert
    alert.accept()
