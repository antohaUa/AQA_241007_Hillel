from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://localhost:80/demo.html")

# Знаходження елемента за XPath з вказанням індексу
li_element = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']")
print(li_element)
li_element = driver.find_element(By.XPATH, "//li[2]")
print(li_element)

# Знаходження всіх елементів з тегом <li>
li_elements = driver.find_elements(By.TAG_NAME, "li")

# Пошук конкретного елемента серед отриманих
for curr_li in li_elements:
    if curr_li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print(f"Знайдено елемент:\n{dir(curr_li)}")
        break
