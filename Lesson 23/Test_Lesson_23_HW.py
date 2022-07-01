from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'http://the-internet.herokuapp.com/dynamic_controls'
        chrome.get(url)
        chrome.fullscreen_window()

        chrome.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        chrome.find_element(By.CSS_SELECTOR, '[onclick="swapCheckbox()"]').click()
        chrome.implicitly_wait(3)
        text = chrome.find_element(By.CSS_SELECTOR, '[id="message"]').text
        assert text == "It's gone!"

        length = len(chrome.find_elements(By.CSS_SELECTOR, '[type="checkbox"]'))
        assert length == 0

        bol = chrome.find_element(By.CSS_SELECTOR, '[type="text"]').is_enabled()
        assert bol == False

        chrome.find_element(By.CSS_SELECTOR, '[onclick="swapInput()"]').click()

        text1 = WebDriverWait(chrome, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '[id="message"]'))).text
        assert text1 == "It's enabled!"

        bol1 = chrome.find_element(By.CSS_SELECTOR, '[type="text"]').is_enabled()
        assert bol1 == True

    finally:
        time.sleep(3)
        chrome.quit()


def test1():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'http://the-internet.herokuapp.com/frames'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(2)

        chrome.find_element(By.CSS_SELECTOR, '[href="/iframe"]').click()
        time.sleep(2)

        chrome.switch_to.frame(chrome.find_element(By.CSS_SELECTOR, '[id="mce_0_ifr"]'))
        text2 = chrome.find_element(By.CSS_SELECTOR, '.mce-content-body>:nth-child(1)')
        text3 = text2.text
        assert text3 == "Your content goes here."

    finally:
        time.sleep(3)
        chrome.quit()
