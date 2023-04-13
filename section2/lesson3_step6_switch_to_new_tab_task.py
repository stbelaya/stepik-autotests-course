from selenium import webdriver
from selenium.webdriver.common.by import By

from aux_methods import copy_code, find_answer

'''Задание: переход на новую вкладку'''

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # press button
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # выбрать вторую вкладку
    new_window = browser.window_handles[1]

    # перейти на вкладку
    browser.switch_to.window(new_window)

    # пройти робокапчу
    find_answer(browser)

    # нажать кнопку Submit
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # выводим код прохождения таски в консоль
    copy_code(browser)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
