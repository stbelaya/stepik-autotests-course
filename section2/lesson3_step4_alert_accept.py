from selenium import webdriver
from selenium.webdriver.common.by import By

from aux_methods import find_answer, copy_code

'''Задание: принимаем alert'''

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # нажать кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # закрыть - принять
    confirm = browser.switch_to.alert
    confirm.accept()

    # решить капчу для роботов
    find_answer(browser)

    # нажать кнопку Submit
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # автоматически копируем код из всплывающего окошка
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
