from selenium import webdriver
from selenium.webdriver.common.by import By
import math

from aux_methods import copy_code

'''Задание: кликаем по checkboxes и radiobuttons (капча для роботов)'''


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # вводим ответ в поле
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # автоматически копируем код из всплывающего окошка
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
