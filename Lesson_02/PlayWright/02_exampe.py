import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dobrobut.com/ua")
    page.get_by_role("banner").get_by_role("link", name="Лікарі").click()
    page.get_by_text("п", exact=True).click()
    page.get_by_role("link", name="2", exact=True).click()
    page.get_by_role("link", name="Петренко Людмила Володимирівна").click()
    page.get_by_text("відгуків").first.click()
    page.get_by_text("QR").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
