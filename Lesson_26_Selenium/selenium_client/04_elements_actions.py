from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.get("http://localhost:80/elements.html")

# Знаходження текстових полів за ID і введення тексту
username_field = driver.find_element(By.XPATH, ".//input[@id='username']")
username_field.send_keys("example_username")
time.sleep(1)

password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys("example_password")

# Знаходження радіо кнопок за ID і вибір варіанта
male_radio = driver.find_element(By.ID, "male")
male_radio.click()
time.sleep(3)

# Знаходження чекбоксу за ID і встановлення прапорця
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()
time.sleep(3)

# Вибір значення з випадаючого списку за ID
country_dropdown = Select(driver.find_element(By.ID, "country"))
print(*dir(country_dropdown), sep='\n')
country_dropdown.select_by_visible_text("США")
time.sleep(3)

# all_selected_options
# deselect_all
# deselect_by_index
# deselect_by_value
# deselect_by_visible_text
# first_selected_option
# is_multiple
# options
# select_by_index
# select_by_value
# select_by_visible_text


# Натискання на кнопку за ID
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# # Зачекати 5 секунд перед завершенням
# time.sleep(5)

# Закрити браузер
driver.quit()