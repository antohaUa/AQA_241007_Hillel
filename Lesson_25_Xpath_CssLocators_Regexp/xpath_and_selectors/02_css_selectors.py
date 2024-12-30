# https://www.selenium.dev/documentation/webdriver/elements/locators/
# https://try.jsoup.org/

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

# By element ID
element = driver.find_element(By.CSS_SELECTOR, "#element_id")

# By element class
element = driver.find_element(By.CSS_SELECTOR, ".class_name")

# By element tag name
element = driver.find_element(By.CSS_SELECTOR, "tag_name")

# By element attribute
element = driver.find_element(By.CSS_SELECTOR, "[attribute_name='value']")

# By attribute starting with specific value
element = driver.find_element(By.CSS_SELECTOR, "[attribute_name^='start_with']")

# By attribute ending with specific value
element = driver.find_element(By.CSS_SELECTOR, "[attribute_name$='end_with']")

# By attribute containing specific value
element = driver.find_element(By.CSS_SELECTOR, "[attribute_name*='contains']")

# By child element
element = driver.find_element(By.CSS_SELECTOR, ".parent_class > span")

# By child element with specific class
element = driver.find_element(By.CSS_SELECTOR, ".parent_class .child_class")