from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ініціалізуємо драйвер Chrome
driver = webdriver.Chrome()

# Відкриваємо головну сторінку
driver.get("http://localhost:80/scroll_frame.html")

# Знаходимо елемент scrollbar на сторінці
scrollbar = driver.find_element(By.XPATH, '//div[@style="height: 1000px; background-color: #f0f0f0;"]')
time.sleep(2)

# Прокрутка вниз
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Прокрутка вгору
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# Переходимо у фрейм
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Натискаємо кнопку три рази
for _ in range(3):
    button = driver.find_element(By.ID, "myButton")
    button.click()
    time.sleep(1)  # Даємо час для реакції на натискання кнопки

# Закриваємо браузер
driver.quit()
