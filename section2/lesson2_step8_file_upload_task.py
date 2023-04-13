import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from aux_methods import copy_code

'''Задание: загрузка файла'''

with open("sw00.txt", "w") as file:
    content = file.write("sw00")  # create test sw00.txt file

file_path = os.getcwd() + '/' + file.name
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # заполняем текстовые поля
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Sveta")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("White")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("sw00@dw.ru")

    # загружаем файл
    file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # автоматически копируем код из всплывающего окошка
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
