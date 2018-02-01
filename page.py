from element import BasePageElement
from locators import CalcPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SetCurrencyValue(BasePageElement):
    locator = ('.rates-aside__filter-block-line-right input')

class GetConvertedValueFrom(BasePageElement):
    locator = CalcPageLocators.CONVERTED_CURRENCY_FROM_VALUE

class GetConvertedValueTo(BasePageElement):
    locator = CalcPageLocators.CONVERTED_CURRENCY_TO_VALUE

class GetDataFromCurrencyFromDropdown(BasePageElement):
    locator = CalcPageLocators.CURRENCY_FROM_VALUE

class GetDataFromCurrencyToDropdown(BasePageElement):
    locator = CalcPageLocators.CURRENCY_TO_VALUE

class GetDataFromCurrencyValueInput(BasePageElement):
    locator = CalcPageLocators.CURRENCY_VALUE_INPUT
    

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class CalcPage(BasePage):
    #Declares a variable that will contain the retrieved text
    set_currency_value = SetCurrencyValue()
    get_converted_value_from = GetConvertedValueFrom()
    get_converted_value_to = GetConvertedValueTo()
    get_data_from_currencyFrom_dropdown = GetDataFromCurrencyFromDropdown()
    get_data_from_currencyTo_dropdown = GetDataFromCurrencyToDropdown()
    get_data_from_currencyValue_input = GetDataFromCurrencyValueInput()

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
