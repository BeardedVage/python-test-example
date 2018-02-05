from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement():

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property    
    def element(self):
        """Gets the text of the specified object"""
        driver = self.driver
        element = WebDriverWait(driver, 8).until(EC.presence_of_element_located(self.locator))
        return element

    @element.setter
    def element(self, value):
        """Sets the text to the value supplied"""
        driver = self.driver
        element = WebDriverWait(driver, 8).until(EC.presence_of_element_located(self.locator))
        element.clear()
        element.send_keys(value)
