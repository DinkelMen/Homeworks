from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_2():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'http://demo.guru99.com/test/newtours/register.php'
        chrome.get(url)
        chrome.fullscreen_window()
        time.sleep(1)
        input_field = chrome.find_element(By.CSS_SELECTOR, '[name=firstName]')
        input_field.send_keys('Dima')
        time.sleep(1)
        input_field1 = chrome.find_element(By.CSS_SELECTOR, '[name=lastName]')
        input_field1.send_keys('Borodin')
        time.sleep(1)
        input_field2 = chrome.find_element(By.CSS_SELECTOR, '[name=phone]')
        input_field2.send_keys('23242342')
        time.sleep(1)
        input_field3 = chrome.find_element(By.CSS_SELECTOR, '[id=userName]')
        input_field3.send_keys('dvd@dvd.com')
        time.sleep(1)

        input_field4 = chrome.find_element(By.CSS_SELECTOR, '[name=address1]')
        input_field4.send_keys('ul. Pushkina')
        time.sleep(1)
        input_field5 = chrome.find_element(By.CSS_SELECTOR, '[name=city]')
        input_field5.send_keys('Bobruisk')
        time.sleep(1)
        input_field6 = chrome.find_element(By.CSS_SELECTOR, '[name=state]')
        input_field6.send_keys('oblast')
        time.sleep(1)
        input_field7 = chrome.find_element(By.CSS_SELECTOR, '[name=postalCode]')
        input_field7.send_keys('345678')
        time.sleep(1)
        input_field8 = Select(chrome.find_element(By.CSS_SELECTOR, '[name=country]'))
        input_field8.select_by_value('BELARUS')
        time.sleep(1)
        input_field9 = chrome.find_element(By.CSS_SELECTOR, '[id=email]')
        input_field9.send_keys('Dima')
        time.sleep(1)
        input_field10 = chrome.find_element(By.CSS_SELECTOR, '[name=password]')
        input_field10.send_keys('qwerty')
        time.sleep(1)
        input_field11 = chrome.find_element(By.CSS_SELECTOR, '[name=confirmPassword]')
        input_field11.send_keys('qwerty')
        time.sleep(1)
        chrome.find_element(By.CSS_SELECTOR, '[name=submit]').click()

        input1 = chrome.find_element(By.XPATH, '(.//tr//table//font)[4]').text
        input2 = chrome.find_element(By.XPATH, '(.//tr//table//font)[6]').text

        assert input1 == 'Dear Dima Borodin,'
        assert input2 == 'Note: Your user name is Dima.'

    finally:
        time.sleep(3)
        chrome.quit()
