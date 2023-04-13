from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from aux_methods import copy_code, find_answer

'''Задание: ждем нужный текст на странице'''

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет равной 100 долларам
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    # пройти робокапчу
    find_answer(browser)

    # нажать кнопку Submit
    button = browser.find_element(By.ID, "solve")
    button.click()

    # выводим код прохождения таски в консоль и копируем в буфер обмена
    copy_code(browser)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
