from base_page import BasePage
from main_page_loc import MainPageLoc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MainPage(BasePage):

    locator = ''

    def open_login_page(self):
        time.sleep(1)
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLoc.login_loc))
        login_link = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.login_loc))
        login_link.click()

    # def verify_login_url(self):

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Login link is not present!"

    def verify_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def press_button(self):
        time.sleep(1)
        button = self.chrome.find_element(*MainPageLoc.button_loc)
        button.click()

    def verify_page(self):
        time.sleep(1)
        cart_title = self.chrome.find_element(*MainPageLoc.verify_page_loc).text
        assert cart_title == 'SHOPPING-CART SUMMARY'

    # , f'{cart_title}hello world'

    def go_to_customer_page(self):
        time.sleep(1)
        customer = self.chrome.find_element(*MainPageLoc.customer_loc)
        customer.click()
