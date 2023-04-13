from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''Задание c пир-ревью: найти уникальные селекторы, чтобы тест нашёл баг в форме регистрации 2 (NoSuchElementException)
и успешно прошёл для правильной формы регистрации 1'''

try:
    # чтобы запустить тест для первой формы регистрации, раскомментируйте следующую строчку
    # link = "http://suninjuly.github.io/registration1.html"
    # чтобы запустить тест для первой формы регистрации, закомментируйте следующую строчку
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    # используются CSS-селекторы по тегу input, атрибуту required и классу first/second/third
    first_name = browser.find_element(By.CSS_SELECTOR, "input[required].first")
    first_name.send_keys("Svetlana")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[required].second")
    last_name.send_keys("Belaya")
    email = browser.find_element(By.CSS_SELECTOR, "input[required].third")
    email.send_keys("sw00@sw.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
