import math

import pyperclip as pc
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def copy_code(browser):
    code = browser.switch_to.alert.text.split(": ")[-1]
    print(code)
    # и копируем в буфер обмена
    pc.copy(code)


def find_answer(browser):
    # находим значение x и считаем формулу
    x = browser.find_element(By.ID, "input_value").text
    value = calc(x)
    # вводим ответ в поле ввода
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(value)
    # press Submit button
    button = browser.find_element(By.ID, "solve")
    button.click()
