import unittest
from selenium import webdriver
import page

class RozetkaSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://rozetka.com.ua/")

    def test_search_in_rozetka(self):
        """
        Tests rozetka search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "rozetka" is in title
        assert main_page.is_title_matches(), "rozetka,com.ua title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "диван"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
        search_results_page.filter_min="100"
        search_results_page.filter_max="7000"
        search_results_page.apply_filters()
        search_results_page.filter_country="Украина"
        item_page = page.ItemPage(self.driver)
        price = item_page.get_result()
        assert (price<7000), "Invalid price"
        cart_page = page.CartPage(self.driver)
        cart_page.to_checkout()
        assert cart_page.is_price_valid(price), "Invalid price"
        print("Her")
        checkout_page = page.CheckoutPage(self.driver)
        print("Here1")
        checkout_page.name = "Иван"
        print("There")
        checkout_page.mail = "rulon_oboev@gmail.com"
        checkout_page.phone = "+380446666666"
        checkout_page.checkout()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()