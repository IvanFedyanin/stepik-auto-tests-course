from selenium import webdriver
import time
import math

try:

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value") # находит текст который указан в элементе
    x = x_element.text

    # Ваш код, который заполняет обязательные поля плюс считаю выражение
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()