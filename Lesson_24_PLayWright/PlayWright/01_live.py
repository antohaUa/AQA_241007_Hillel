from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1/demo.html")
    page.get_by_label("Ім'я користувача:").click()
    page.get_by_label("Ім'я користувача:").fill("user1")
    page.get_by_label("Пароль:").click()
    page.get_by_label("Пароль:").fill("test1")
    page.get_by_text("Ім'я користувача: Пароль: Увійти").click()
    page.get_by_role("button", name="Увійти").click()
    page.get_by_text("Елемент списку 2").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
