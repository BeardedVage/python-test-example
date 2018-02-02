import pytest
from selenium import webdriver


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = webdriver.Chrome()
    browser.get("http://www.sberbank.ru/ru/quotes/converter")
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

