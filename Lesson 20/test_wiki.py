from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_wiki_search_field():
    url = 'https://ru.wikipedia.org/wiki/'
    word = 'Автоматизация'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)
    time.sleep(3)
    search_input = chrome.find_element(By.ID, "search_input")
    search_input.send_keys(word)
    search_input.submit()
    time.sleep(2)
    title = chrome.find_element(By.ID, 'firstHeading').text
    assert word == title, f'{title} is not eq {word}'
