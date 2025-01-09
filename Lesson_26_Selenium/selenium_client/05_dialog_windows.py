from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.get("http://localhost:80/dialog.html")

# Показати Alert і отримати текст з нього
button1 = driver.find_element(By.XPATH, "//button[text()='Показати Alert']")
button1.click()
time.sleep(3)
alert = Alert(driver)
print("Текст Alert:", alert.text)
alert.accept()

# Показати Confirm і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
alert = Alert(driver)
time.sleep(3)
print("Текст Confirm:", alert.text)
print(*dir(alert), sep='\n')
alert.dismiss()

# Показати Prompt, ввести текст і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
time.sleep(3)
alert = Alert(driver)
print("Текст Prompt:", alert.text)
alert.send_keys("Python")
alert.accept()

# Зачекати 2 секунди перед завершенням
time.sleep(2)

# Закрити браузер
driver.quit()