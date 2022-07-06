from selenium import webdriver
from main_page_loc import MainPageLoc
import pytest
import time
chrome = webdriver.Chrome('./chromedriver')


@pytest.fixture()
def open_base_page():
    url = 'http://automationpractice.com/index.php'
    chrome.get(url)


def test_1(open_base_page):
    try:
        time.sleep(3)
        chrome.find_element(*MainPageLoc.cart_loc).click()
        status = chrome.find_element(*MainPageLoc.cart_empty_2).text
        assert status == 'Your shopping cart is empty.'
    finally:
        chrome.quit()


def test_2(open_base_page):
    try:
        time.sleep(3)
        chrome.find_element(*MainPageLoc.login_loc).click()
        sub_log = chrome.find_element(*MainPageLoc.submit_login_button)
        sub_log.click()
    finally:
        chrome.quit()
