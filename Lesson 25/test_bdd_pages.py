import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from main_page import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from customer_page import CustomerPage
global main_page

scenarios('./test_bdd_page.feature')


@pytest.fixture
def open_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@given('We open main page.')
def open_site(open_browser):
    link = "http://automationpractice.com/index.php"
    global main_page
    main_page = MainPage(open_browser, link)
    main_page.open()


@when('We press the button.')
def press_button():
    main_page.press_button()


@then('Check where we are.')
def verify_page():
    main_page.verify_page()


# def test_check(open_browser):
#     time.sleep(2)
#     open_site(open_browser)
#     time.sleep(2)
#     press_button()
#     time.sleep(2)
#     verify_page()

