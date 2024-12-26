import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:80/demo.html")

    page.get_by_label("Ім'я користувача:").click()
    time.sleep(1)
    page.get_by_label("Ім'я користувача:").fill("user")
    page.get_by_label("Пароль:").click()
    time.sleep(1)
    page.get_by_label("Пароль:").fill("pass")
    page.get_by_role("button", name="Увійти").click()
    time.sleep(1)
    page.get_by_text("Елемент списку 2").click()
    time.sleep(1)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
