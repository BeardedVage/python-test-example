from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        element = WebDriverWait(driver, 8).until(EC.presence_of_element_located(self.locator))
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        element = WebDriverWait(driver, 8).until(EC.presence_of_element_located(self.locator))
        return element

