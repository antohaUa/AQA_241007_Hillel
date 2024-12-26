from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:80/demo.html")

    # Знаходження елемента за XPath з вказанням індексу
    li_element = page.query_selector("//li[.='Елемент списку 2']")
    print(li_element)
    li_element = page.query_selector("//li[3]")
    print(li_element)

    # Знаходження всіх елементів з тегом <li>
    li_elements = page.query_selector_all("li")

    # Пошук конкретного елемента серед отриманих
    for curr_li in li_elements:
        # breakpoint()
        if curr_li.inner_text() == "Елемент списку 2":
            # Знайдено потрібний елемент
            print(f"Знайдено елемент:\n{dir(curr_li)}")
            break

    browser.close()
