import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Flask app URL
BASE_URL = "http://127.0.0.1:8080"
ALLOWED_USER_AGENT = "MyCustomAgent/1.0"
ALLOWED_COOKIE = {"name": "visit_id", "value": "12345"}


class TestAgentCookies:
    @pytest.fixture
    def browser(self):
        options = Options()
        options.add_argument(f'user-agent={ALLOWED_USER_AGENT}')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    def test_flask_app_access(self, browser):
        # Open the page to set the allowed cookie
        browser.get(f"{BASE_URL}/")

        # Add the allowed cookie manually (if necessary)
        browser.add_cookie({
            "name": ALLOWED_COOKIE["name"],
            "value": ALLOWED_COOKIE["value"],
            "path": "/"
        })

        # Navigate to the home page
        browser.get(BASE_URL)

        # Verify the page title and content
        assert "Welcome Page" in browser.title

        # Check for the congratulations message
        congrats_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations!" in congrats_text

        # Check for the correct user-agent and visit ID displayed
        user_agent_text = browser.find_element(By.XPATH, "//p[contains(text(), 'user-agent')]").text
        assert ALLOWED_USER_AGENT in user_agent_text

        visit_id_text = browser.find_element(By.XPATH, "//p[contains(text(), 'visit ID')]").text
        assert ALLOWED_COOKIE["value"] in visit_id_text

        # Save a screenshot of the home page
        browser.save_screenshot("congratulations_page.png")

    def test_flask_app_invalid_user_agent(self):
        default_options = Options()
        default_driver = webdriver.Chrome(options=default_options)
        default_driver.get(BASE_URL)

        # Verify access is denied
        assert "Access Denied" in default_driver.page_source

        default_driver.quit()
