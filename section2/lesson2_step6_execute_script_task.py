from selenium import webdriver
from selenium.webdriver.common.by import By

from aux_methods import copy_code, find_answer

'''Задание на execute_script'''

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # находим значение x и считаем формулу, вводим ответ в поле ввода (общий код вынесен в отдельный модуль
    find_answer(browser)

    # Выбираем чекбокс и скроллим вниз, чтобы он был доступен
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_robot)
    checkbox_robot.click()

    # переключаем радиобаттон
    radio_robot = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
    radio_robot.click()

    # press Submit
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # автоматически копируем код из всплывающего окошка
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
