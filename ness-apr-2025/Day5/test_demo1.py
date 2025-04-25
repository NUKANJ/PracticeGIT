import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ebay.com")

    #if ID is fancy then we can search by this
    #driver.find_element(By.CSS_SELECTOR,"#fancy")

    # <div class='t1 t2 t3'>
    # </div>
    #
    # driver.find_element(By.CLASS_NAME,"t1 t2 t3")
    # driver.find_element(By.CSS_SELECTOR,".t1")

    #time.sleep()- will pause the test execution for the time specifies
    #implicit wait - will wait till the element is present
    #                will pause for the time specified if the element is not present.
    #                NoSuchElementException
    #Explicit wait - Specific conditions attached to it
    #                WebdriverWait class is used
    #                polling frequency - 500ms
    #                TimeoutException
    #Fluent Wait - Extension of explicit wait
    #              polling frequency can be set
    #              ignore exceptions
    #




