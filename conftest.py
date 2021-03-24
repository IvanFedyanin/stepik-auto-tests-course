import pytest
from selenium import webdriver
#в файл вынесена фикстура которая содаёт экземпляр браузера, файл применяется ко всем тестам в папке
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()