import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    #browser.quit()

@pytest.mark.parametrize('lession', ["236895/step/1","236896/step/1","236897/step/1","236898/step/1","236899/step/1","236903/step/1","236904/step/1","236905/step/1"])
def test_link_lession(browser,lession):
    link = f"https://stepik.org/lesson/{lession}"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    print(answer)
    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    message = browser.find_element_by_class_name("smart-hints__hint")

    srav  = message.text
    print(srav)

    assert srav == "Correct!"



