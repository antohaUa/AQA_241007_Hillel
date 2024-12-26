from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:80/demo.html")

    # Знаходження елемента за ID
    username_field = page.query_selector("#username")
    password_field = page.query_selector("#password")
    login_button = page.query_selector("#login_button")

    # Знаходження елемента за XPath
    username_field = page.query_selector("//html/body/form/input[@id='username']")
    password_field = page.query_selector("//input[@id='password']")
    login_button = page.query_selector("//button[@id='login_button']")
    #
    # Знаходження елемента за CSS класом
    username_field = page.query_selector(".input-field#username")
    password_field = page.query_selector(".input-field#password")
    login_button = page.query_selector("#login_button")
    #
    # Знаходження елемента за назвою тегу
    form_element = page.query_selector("form")
    print("Success!")

    browser.close()
