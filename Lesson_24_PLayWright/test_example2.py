import os
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

base_url = "https://www.saucedemo.com/"


class TestSauceDemo:
    @pytest.fixture(scope='class')
    def main_page(self):
        with sync_playwright() as playwright:
            # getattr(playwright, 'chromium')
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(base_url)
            yield page
            context.close()
            browser.close()

    def test_action(self, main_page):
        # main_page.locator("[data-test=\"login-credentials\"]").click()
        # main_page.locator("[data-test=\"login-credentials\"]").click()
        username = main_page.locator("[data-test=\"username\"]")
        username.fill("standard_user")
        main_page.locator("[data-test=\"password\"]").click()
        main_page.locator("[data-test=\"password\"]").fill("secret_sauce")
        main_page.locator("[data-test=\"login-button\"]").click()
        main_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        main_page.locator("[data-test=\"shopping-cart-link\"]").click()
        main_page.locator("[data-test=\"item-4-title-link\"]").click()
        main_page.locator("[data-test=\"remove\"]").click()
        main_page.locator("[data-test=\"back-to-products\"]").click()
        main_page.get_by_role("button", name="Open Menu").click()
        main_page.locator("[data-test=\"logout-sidebar-link\"]").click()

