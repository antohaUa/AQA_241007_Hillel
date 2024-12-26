from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:80/elements.html")

    # Знаходження текстових полів за ID і введення тексту
    time.sleep(2)
    username_field = page.query_selector("#username")
    username_field.fill("example_username")
    time.sleep(2)

    password_field = page.query_selector("#password")
    password_field.fill("example_password")

    # Знаходження радіо кнопок за ID і вибір варіанта
    male_radio = page.query_selector("#male")
    male_radio.click()
    time.sleep(3)

    # Знаходження чекбоксу за ID і встановлення прапорця
    newsletter_checkbox = page.query_selector("#newsletter")
    newsletter_checkbox.click()
    time.sleep(3)
    #
    # Вибір значення з випадаючого списку за ID
    page.select_option("#country", value="usa")
    time.sleep(3)

    # Натискання на кнопку за ID
    submit_button = page.query_selector("#submit")
    submit_button.click()

    browser.close()
