from selenium import webdriver
from main_page_loc import MainPageLoc


class BasePage:
    def __init__(self):
        self.base_page_link = 'http://automationpractice.com/index.php'
        self.chrome = webdriver.Chrome('./chromedriver')
        self.chrome.implicitly_wait(5)

    def open_base_page(self):
        self.chrome.get(self.base_page_link)

    def check_base_page(self):
        base_page_title = self.chrome.find_element(*MainPageLoc.base_page_title_loc)
        assert base_page_title == 'My store'
