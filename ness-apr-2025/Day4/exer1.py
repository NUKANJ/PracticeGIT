import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pytest


def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.ebay.com/?msockid=142f15fecf4d6b600e33005bce1f6ae1")
    time.sleep(3)

    driver.maximize_window()

    driver.find_element(By.CLASS_NAME, 'gh-search-input').send_keys("Selenium")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'gh-search-categories').click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//option[@value='267']").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'gh-search-button').click()
    time.sleep(2)

    #driver.find_element(By.CLASS_NAME,'srp-format-tabs-h2').click()
    #time.sleep(2)

    driver.find_element(By.PARTIAL_LINK_TEXT, 'Buy It Now').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@aria-label='Sort selector. Best Match selected.']").click()
    time.sleep(2)

    driver.find_element(By.PARTIAL_LINK_TEXT,'newly listed').click()

    asser = driver.find_element(By.CSS_SELECTOR,"span.s-item__listingDate > span")

    time.sleep(5)
    assert asser.is_displayed() == True
    #assert asser.text == "Apr"





