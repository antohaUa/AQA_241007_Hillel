import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# iніціалізуємо веб-драйвер
driver = Chrome()

# Відкриття сторінки
driver.get("http://localhost:80/drop_down_menu.html")

# cтворюємо екземпляр класу ActionChains
actions = ActionChains(driver)

# Знайти кнопку "Menu"
time.sleep(1)
menu_button = driver.find_element(By.TAG_NAME, "button")

# Навести курсор на кнопку "Menu", щоб відобразити випадаюче меню
actions.move_to_element(menu_button).perform()

# Знайти всі посилання на продукти в меню "Products"
product_links = driver.find_elements(By.CSS_SELECTOR, ".dropdown-submenu .dropdown-content .product-link")

# Пройтися по кожному посиланню і натиснути його
for link in product_links:
    # https://selenium-python.readthedocs.io/waits.html
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "button")))
    actions.move_to_element(link).perform()
    actions.click(link).perform()
    time.sleep(1)
    # Почекати, поки з'явиться діалогове вікно підтвердження
    WebDriverWait(driver, 5).until(EC.alert_is_present())

    time.sleep(1)
    # Підтвердити діалогове вікно
    # alert = Alert(driver)
    alert = driver.switch_to.alert
    alert.accept()

# Закриття веб-драйвера
driver.quit()
