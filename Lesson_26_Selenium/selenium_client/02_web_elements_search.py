from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://localhost:80/demo.html")

# Знаходження елемента за ID
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")

# Знаходження елемента за XPath
username_field2 = driver.find_element(By.XPATH, "//html/body/form/input[@id='username']")
password_field2 = driver.find_element(By.XPATH, "//input[@id='password']")
login_button2 = driver.find_element(By.XPATH, "//button[@id='login_button']")
#
# Знаходження елемента за CSS класом
username_field3 = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
password_field3 = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
login_button3 = driver.find_element(By.CSS_SELECTOR, "#login_button")

# Знаходження елемента за назвою тегу
form_element = driver.find_element(By.TAG_NAME, "form")
print('Success!')
driver.quit()
