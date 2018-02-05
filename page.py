from element import BasePageElement
from locators import CalcPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class CalcPage(BasePage):

    def get_data_from_currencyFrom_dropdown(self):
        getter = BasePageElement(self.driver, CalcPageLocators.CURRENCY_FROM_VALUE)
        return getter.element

    def get_data_from_currencyTo_dropdown(self):
        getter = BasePageElement(self.driver, CalcPageLocators.CURRENCY_TO_VALUE)
        return getter.element

    def get_data_from_currencyValue_input(self):
        getter = BasePageElement(self.driver, CalcPageLocators.CURRENCY_VALUE_INPUT)
        return getter.element

    def get_converted_value_to(self):
        getter = BasePageElement(self.driver, CalcPageLocators.CONVERTED_CURRENCY_TO_VALUE)
        return getter.element

    def get_converted_value_from(self):
        getter = BasePageElement(self.driver, CalcPageLocators.CONVERTED_CURRENCY_FROM_VALUE)
        return getter.element

    def set_currency_value(self, value):
        setter = BasePageElement(self.driver, CalcPageLocators.CURRENCY_VALUE_INPUT)
        setter.element(value)

    def is_calculation_finished(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((CalcPageLocators.RESULT_BODY)))

    def choose_currency_from(self, curr_name):
        self.driver.execute_script("$(\"select\").css(\"display\", \"block\");")
        Select(self.driver.find_element_by_css_selector("select[name=\"converterFrom\"]")).select_by_visible_text(curr_name)

    def click_convert_button(self):
        element = self.driver.find_element(*CalcPageLocators.CONVERT_BUTTON)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.click()

