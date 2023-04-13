from selenium import webdriver
from selenium.webdriver.common.by import By

from aux_methods import copy_code, calc

'''Задание: поиск сокровища с помощью get_attribute'''


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим x
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
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
