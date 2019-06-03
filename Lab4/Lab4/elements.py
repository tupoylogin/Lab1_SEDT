from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement(object):
    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        self.value = value
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).click()
        #driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(Keys.CONTROL + "a")
        driver.find_element(*self.locator).send_keys(self.value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


class CheckBoxElement(BasePageElement):

     def __set__(self, obj, value):
        """Sets the text to the value supplied. For checkboxes value automatically sets to none"""
        value=None
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).click()

     def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")

class FilterElement(BasePageElement):

    def __set__(self, obj, value):
        """Sets the text to the value supplied."""
        country = '\''+value+'\')]'
        func,method=self.locator
        method+=country
        driver = obj.driver
        #print(method)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(func,method))
        driver.find_element(func,method).find_element_by_xpath('.//a').click()

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")

class ContactFieldElement(BasePageElement):

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        self.value = value
        driver.find_element(*self.locator).send_keys(self.value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")