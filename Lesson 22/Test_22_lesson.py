from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/complicated-page/'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(1)
        chrome.find_element(By.CLASS_NAME, 'et_pb_button_1.et_pb_bg_layout_light').click()
        time.sleep(1)
        chrome.find_element(By.CSS_SELECTOR, '[class="et_pb_button et_pb_button_1 et_pb_bg_layout_light"]').click()
        time.sleep(1)
        chrome.find_element(By.XPATH, '//a[@class="et_pb_button et_pb_button_1 et_pb_bg_layout_light"]').click()

    finally:
        time.sleep(3)
        chrome.quit()
