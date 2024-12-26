from playwright.sync_api import sync_playwright
import time


def handle_dialog(dialog):
    if dialog.type == "alert":
        print("Текст Alert:", dialog.message)
        time.sleep(1)
        dialog.accept()
    elif dialog.type == "confirm":
        print("Текст Confirm:", dialog.message)
        time.sleep(1)
        dialog.dismiss()
    elif dialog.type == "prompt":
        print("Текст Prompt:", dialog.message)
        time.sleep(1)
        dialog.accept(prompt_text="Python")
        time.sleep(1)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:80/dialog.html")

    page.on("dialog", handle_dialog)
    button1 = page.query_selector("//button[text()='Показати Alert']")
    button1.click()
    time.sleep(2)

    button2 = page.query_selector("//button[text()='Показати Confirm']")
    button2.click()
    time.sleep(2)

    button3 = page.query_selector("//button[text()='Показати Prompt']")
    button3.click()
    time.sleep(2)

    browser.close()
