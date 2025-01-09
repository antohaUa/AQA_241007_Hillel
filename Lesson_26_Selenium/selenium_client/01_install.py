# https://selenium-python.readthedocs.io/
# pip install selenium
from selenium import webdriver

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Chrome()

# Відкриття веб-сторінки
driver.get("https://www.example.com")

# Робота з веб-елементами і виконання дій на сторінці

print('It works')
# Закриття браузера
driver.quit()
