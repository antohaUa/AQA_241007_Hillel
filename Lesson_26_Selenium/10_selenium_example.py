from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = Chrome()
driver.get("https://ultimateqa.com/filling-out-forms/")


input_field1 = driver.find_element(By.XPATH, "//input[@id='et_pb_contact_name_1']")
input_field1.send_keys("example_username")
message_field = driver.find_element(By.XPATH, "//textarea[@id='et_pb_contact_message_1']")
message_field.send_keys(f"example text {Keys.ENTER}example text line 2")
captcha_element = driver.find_element(By.XPATH, "//input[@class ='input et_pb_contact_captcha']")
digit1 = int(captcha_element.get_attribute('data-first_digit'))
digit2 = int(captcha_element.get_attribute('data-second_digit'))
captcha_element.send_keys(f'{digit1+digit2}')
target_buttons = driver.find_elements(By.XPATH, "//button[@name='et_builder_submit_button']")
target_buttons[1].click()
time.sleep(3)

print('Success!')
driver.quit()



