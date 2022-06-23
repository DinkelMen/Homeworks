from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://demoqa.com/select-menu/'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(1)
        input_field = chrome.find_element(By.CSS_SELECTOR, '[id=withOptGroup]')
        time.sleep(1)
        input_field.click()
        time.sleep(1)
        chrome.find_element(By.ID, 'react-select-2-option-0-0').click()

        time.sleep(1)
        input_field1 = chrome.find_element(By.CSS_SELECTOR, '[id=selectOne]')
        time.sleep(1)
        input_field1.click()
        time.sleep(1)
        chrome.find_element(By.ID, 'react-select-3-option-0-0').click()

        input_field2 = Select(chrome.find_element(By.CSS_SELECTOR, '[id=oldSelectMenu]'))
        input_field2.select_by_value('3')

        input_field3 = chrome.find_element(By.CSS_SELECTOR, 'p + [class=" css-2b097c-container"]')
        time.sleep(1)
        input_field3.click()
        time.sleep(1)
        chrome.find_element(By.ID, 'react-select-4-option-0').click()

        input_field4 = Select(chrome.find_element(By.CSS_SELECTOR, '[id=cars]'))
        input_field4.select_by_value('audi')

    finally:
        time.sleep(5)
        chrome.quit()

        # (By.XPATH, "//*[contains(text(), 'Green')]").click()
        # input_field = chrome.find_element(By.CSS_SELECTOR, '[id=userName]')
        # input_field.send_keys('Dima')
        # time.sleep(1)
        # input_field2 = chrome.find_element(By.CSS_SELECTOR, '[id=userEmail]')
        # input_field2.send_keys('dssdfs@dsd.com')
        # time.sleep(1)
        # input_field3 = chrome.find_element(By.CSS_SELECTOR, '[id=currentAddress]')
        # input_field3.send_keys('ul. Pushkina')
        # time.sleep(1)
        # input_field4 = chrome.find_element(By.CSS_SELECTOR, '[id=permanentAddress]')
        # input_field4.send_keys('d. Kolotushkina')
        # time.sleep(2)
        #
        # button = chrome.find_element(By.CSS_SELECTOR, '[id=submit]')
        # time.sleep(2)
        # button.click()
        #
        # text1 = chrome.find_element(By.CSS_SELECTOR, '[id=name]').text
        # text2 = chrome.find_element(By.CSS_SELECTOR, '[id=email]').text
        # text3 = chrome.find_element(By.CSS_SELECTOR, '[id=currentAddress][class=mb-1]').text
        # text4 = chrome.find_element(By.CSS_SELECTOR, '[id=permanentAddress][class=mb-1]').text
        #
        # assert text1 == 'Name:Dima'
        # assert text2 == 'Email:dssdfs@dsd.com'
        # assert text3 == 'Current Address :ul. Pushkina'
        # assert text4 == 'Permanent Address :d. Kolotushkina'
        # time.sleep(4)
