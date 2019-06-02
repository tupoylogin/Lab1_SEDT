from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_BUTTON = (By.XPATH, '//button[@class=\"button button_color_green button_size_medium search-form__submit\"]')
    TEXT_FIELD = (By.NAME, 'search')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    RESULT_WRAP = (By.ID,'search_result_title_text')
    FILTER_PRICE_MIN = (By.ID,'price[min]')
    FILTER_PRICE_MAX = (By.ID,'price[max]')
    FILTER_COUNTRY = (By.XPATH,'//form[@id=\"filter_parameters_form\"]/div/div/ul/li/label[contains(.//a/span/i[1],')
    SUBMIT_BUTTON = (By.ID,'submitprice')


class ItemPageLocators(object):
    """A class for item page locators"""
    RESULT = (By.XPATH,'//div[@name=\"search_list\"]/div[1]')
    TO_CART = (By.XPATH,'//button[@name=\"topurchases\"]')

class CartPageLocators(object):
    CART = (By.XPATH, '//div[@id=\"cart-popup\"]')

class ContactPageLocators(object):
    NAME = (By.CSS_SELECTOR,'#reciever_name')
    #LOCALITY = (By.ID,'suugest_locality')
    PHONE = (By.CSS_SELECTOR,'#reciever_phone')
    MAIL = (By.CSS_SELECTOR,'#reciever_email')
    NXT_BUTTON = (By.XPATH,'//button[@name=\"next_step\"]')
    FORM_LOADED = (By.XPATH,'//form[@id=\"checkout_form\"]')

class DeliveryPageLocators(object):
    RADIO_DELIVERY=(By.XPATH,'//label[@name=\"pickups_1\"]/input')
    RADIO_SUBDELIVERY=(By.XPATH,'//label[@class=\"check-address-label\"]/input')
    PURCHASE_BUTTON = (By.ID, 'make-order')