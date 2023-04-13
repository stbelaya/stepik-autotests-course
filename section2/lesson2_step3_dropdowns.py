from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from aux_methods import copy_code

'''Задание: работа с выпадающим списком'''

try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим заданные числа
    x1 = browser.find_element(By.ID, "num1").text
    x2 = browser.find_element(By.ID, "num2").text
    # находим сумму
    s = int(x1) + int(x2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(s))  # ищем элемент с текстом нашей суммы

    # Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # автоматически копируем код из всплывающего окошка
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
