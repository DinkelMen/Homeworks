from main_page_loc import MainPageLoc
from base_page import BasePage


class LoginPage(BasePage):

    def open_login_page(self):
        login_link = self.chrome.find_element(*MainPageLoc.login_loc)
        login_link.click()

    def check_login_page(self):
        base_page_title = self.chrome.find_element(*MainPageLoc.login_page_title_loc)
        assert base_page_title == 'Login - My store'
