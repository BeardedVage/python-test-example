from selenium.webdriver.common.by import By


class CalcPageLocators(object):
    """A class for calc page locators."""
    CONVERT_BUTTON = (By.CLASS_NAME, 'rates-button')

    RESULT_BODY = (By.CLASS_NAME, 'rates-converter-result')

    CURRENCY_FROM_VALUE = (By.CSS_SELECTOR, 'select[name="converterFrom"] + div strong')

    CURRENCY_TO_VALUE = (By.CSS_SELECTOR, 'select[name="converterTo"] + div strong')

    CURRENCY_VALUE_INPUT = (By.CSS_SELECTOR, '.rates-aside__filter-block-line-right input')

    CONVERTED_CURRENCY_FROM_VALUE = (By.CLASS_NAME, 'rates-converter-result__total-from')

    CONVERTED_CURRENCY_TO_VALUE = (By.CLASS_NAME, 'rates-converter-result__total-to')

    CURRENCY_FROM_DROPDOWN_SELECT = (By.CSS_SELECTOR, 'select[name="converterFrom"] + .select')
