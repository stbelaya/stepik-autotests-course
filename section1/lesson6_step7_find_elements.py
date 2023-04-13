from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from aux_methods import copy_code

'''Задание: использование метода find_elements'''

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("hi")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # автоматически копируем код из всплывающего окошка
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла