from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import MoveTargetOutOfBoundsException
import time

# iніціалізуємо веб-драйвер
driver = Chrome()

# відкриваємо сторінку з прикладом
driver.get("http://localhost:80/action_chains.html")

# знаходимо eлемент circle
circle = driver.find_element(By.ID, "circle")

# cтворюємо екземпляр класу ActionChains
actions = ActionChains(driver)

# отримаємо розміри зони, де ми можемо переміщувати круг
zone = driver.find_element(By.ID, "container")

# дозволена довжина/ширина зони для руху
azw = zone.size['width'] - circle.size['width'] - 10
azh = zone.size['height'] - circle.size['height'] - 10

try:
    # центр зони
    actions.click_and_hold(circle).move_to_element(zone).perform()
    time.sleep(1)
    # правий нижнiй кут
    actions.move_to_element(circle).move_by_offset(azw / 2, azh / 2).perform()
    time.sleep(1)
    # правий верхнiй кут
    actions.move_to_element(circle).move_by_offset(0, -azh).perform()
    time.sleep(1)
    # лiвий верхнiй кут
    actions.move_to_element(circle).move_by_offset(-azw, 0).perform()
    time.sleep(1)
    # лiвий  нижнiй кут
    actions.move_to_element(circle).move_by_offset(0, azh).perform()
    time.sleep(1)
    # центр зони
    actions.click_and_hold(circle).move_to_element(zone).perform()
    time.sleep(1)
    # подвiйний клiк
    actions.double_click(circle).perform()
    time.sleep(1)
    # одинарний клiк
    actions.click(circle).perform()
    time.sleep(1)

    # перевіряємо чи змінився фоновий колір на зелений
    background_color = circle.value_of_css_property("background-color")
    # RGBA значення кольору зеленого (0, 128, 0) з повним непрозорістю (alpha = 1)
    if background_color == "rgba(0, 128, 0, 1)":
        print("Фон змінився на зелений!")

    # курсор поза межi circle
    actions.move_by_offset(-100, -100).perform()
    time.sleep(1)

    # перевіряємо чи змінився фоновий колір на червоний
    background_color_out = circle.value_of_css_property("background-color")
    # RGBA значення кольору red (255, 0, 0) з повним непрозорістю (alpha = 1)
    if background_color_out == "rgba(255, 0, 0, 1)":
        print("Фон змінився на червоний!")

    # натискання клавіші Enter
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(1)
    alert = Alert(driver)
    # закриваємо Confirm вiкно
    alert.accept()
    time.sleep(0.5)
except MoveTargetOutOfBoundsException as bound_err:
    print('Out of bounce!!!')
finally:
    # закриваємо веб-драйвер
    driver.quit()
