from main_page_loc import MainPageLoc
from base_page import BasePage
from selenium import webdriver
chrome = webdriver.Chrome('./chromedriver')


class CartPage(BasePage):

    def open_cart_page(self):
        cart_link = self.chrome.find_element(*MainPageLoc.cart_loc)
        cart_link.click()

    def check_cart_page(self):
        base_page_title = self.chrome.find_element(*MainPageLoc.cart_page_title_loc)
        assert base_page_title == 'Order - My store'
