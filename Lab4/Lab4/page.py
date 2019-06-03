from elements import BasePageElement, CheckBoxElement, FilterElement,ContactFieldElement
from locators import MainPageLocators,SearchResultsPageLocators,ItemPageLocators,CartPageLocators,ContactPageLocators,DeliveryPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = MainPageLocators.TEXT_FIELD

class FilterPriceMinElement(BasePageElement):
    locator = SearchResultsPageLocators.FILTER_PRICE_MIN

class FilterPriceMaxElement(BasePageElement):
    locator = SearchResultsPageLocators.FILTER_PRICE_MAX

class FilterCountryElement(FilterElement):
    locator = SearchResultsPageLocators.FILTER_COUNTRY

class NameElement(ContactFieldElement):
    locator = ContactPageLocators.NAME

class MailElement(ContactFieldElement):
    locator = ContactPageLocators.MAIL

class PhoneElement(ContactFieldElement):
    locator = ContactPageLocators.PHONE


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Rozetka" appears in page title"""
        return "rozetka" in self.driver.title.lower()

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    filter_min = FilterPriceMinElement()
    filter_max = FilterPriceMaxElement()
    filter_country = FilterCountryElement()

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def apply_filters(self):
        element = self.driver.find_element(*SearchResultsPageLocators.SUBMIT_BUTTON)
        element.click()

class ItemPage(BasePage):

    def get_result(self):
        result = self.driver.find_element(*ItemPageLocators.RESULT)
        price = result.find_element_by_xpath('.//div[@name=\"prices_active_element_original\"]/div/div[@name=\"price\"]/div/span[1]')
        price = int(price.text.replace(" ",""))
        cart_element = self.driver.find_element(*ItemPageLocators.TO_CART)
        cart_element.click()
        return price


class CartPage(BasePage):

    def load_cart(self):
        WebDriverWait(self.driver, 150).until(EC.presence_of_element_located(CartPageLocators.CART))
        cart = self.driver.find_element(*CartPageLocators.CART)
        self._price=int(cart.find_element_by_xpath('.//span[@name=\"cost\"]').text.replace(" ",""))
        return cart
   
    def is_price_valid(self,price):
        return price==self._price
    
    def to_checkout(self):
        button = self.load_cart().find_element_by_xpath('.//form[@id=\"drop-block\"]/span/span/button')
        button.click()


class CheckoutPage(BasePage):
    name = NameElement()
    mail = MailElement()
    phone = PhoneElement()

    def checkout(self):

        #element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ContactPageLocators.NXT_BUTTON))
        element = self.driver.find_element(*ContactPageLocators.NXT_BUTTON).click()
        
        radio1=self.driver.find_element(*DeliveryPageLocators.RADIO_DELIVERY)
        if not (radio1.is_selected()):
            radio1.click()
        WebDriverWait(self.driver, 20).until(self.driver.find_element(*DeliveryPageLocators.RADIO_SUBDELIVERY))
        radio2=self.driver.find_element(*DeliveryPageLocators.RADIO_SUBDELIVERY).find_element_by_xpath('.//a')
        radio2.click()
        list = self.driver.find_element(*DeliveryPageLocators.RADIO_SUBDELIVERY).find_element_by_xpath('.//div/div[2]/ul/li[1]/a').click()
        purchase = self.driver.find_element(*DeliveryPageLocators.PURCHASE_BUTTON)
        purchase.click()


