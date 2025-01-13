import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://127.0.0.1/appear_disappear.html'


# Setup WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def test_element_disappearance_and_appearance(driver):
    # Find the initial old element and verify it is visible
    old_element = driver.find_element(By.ID, 'oldElement')
    assert old_element.is_displayed(), "Old element should be visible initially"

    # Find the new element and ensure it is not visible
    new_element = driver.find_element(By.ID, 'newElement')
    assert not new_element.is_displayed(), "New element should be hidden initially"

    # Click the button to trigger the toggle
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    # Wait for a moment to ensure the page updates
    driver.implicitly_wait(2)

    # Verify the old element disappears
    assert not old_element.is_displayed(), "Old element should be hidden after button click"

    # Verify the new element appears
    assert new_element.is_displayed(), "New element should be visible after button click"
