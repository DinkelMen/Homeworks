from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test2():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(1)
        input_field1 = chrome.find_element(By.CSS_SELECTOR, '[id="et_pb_contact_name_0"]')
        input_field1.send_keys('Dima')
        time.sleep(1)
        input_field2 = chrome.find_element(By.CSS_SELECTOR, '[id="et_pb_contact_message_0"]')
        input_field2.send_keys('Hello world!')
        time.sleep(1)
        input_field3 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_module.et_pb_contact_form_0.et_pb_contact_form_container.clearfix>:nth-child(2)>:nth-child(1)>:nth-child(4)>:nth-child(1)')
        input_field3.click()
        time.sleep(5)

        input_field4 = chrome.find_element(By.CSS_SELECTOR, '.et-pb-contact-message>:nth-child(1)')
        input_text = input_field4.text
        assert input_text == 'Thanks for contacting us'

    finally:
        time.sleep(3)
        chrome.quit()


def test3():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(1)
        input_field5 = chrome.find_element(By.CSS_SELECTOR, '[id="et_pb_contact_name_0"]')
        input_field5.send_keys('Dima')
        time.sleep(1)
        input_field6 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_module.et_pb_contact_form_0.et_pb_contact_form_container.clearfix>:nth-child(2)>:nth-child(1)>:nth-child(4)>:nth-child(1)')
        input_field6.click()
        time.sleep(3)

        input_field = chrome.find_element(By.CSS_SELECTOR, '.et-pb-contact-message>:nth-child(1)')
        input_text = input_field.text
        assert input_text == 'Please, fill in the following fields:'

    finally:
        time.sleep(3)
        chrome.quit()


def test4():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(1)
        input_field7 = chrome.find_element(By.CSS_SELECTOR, '[id="et_pb_contact_message_0"]')
        input_field7.send_keys('Hello world!')
        time.sleep(1)
        input_field8 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_module.et_pb_contact_form_0.et_pb_contact_form_container.clearfix>:nth-child(2)>:nth-child(1)>:nth-child(4)>:nth-child(1)')
        input_field8.click()
        time.sleep(3)

        input_field = chrome.find_element(By.CSS_SELECTOR, '.et-pb-contact-message>:nth-child(1)')
        input_text = input_field.text
        assert input_text == 'Please, fill in the following fields:'

    finally:
        time.sleep(3)
        chrome.quit()
