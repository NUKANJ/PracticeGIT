import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.chrome import ChromeDriverManager

# test method
from selenium.webdriver.common.by import By


def test_googletest():
    os.chdir("../lib")
    # print(os.getcwd())

    # launch the browser
    service = Service(executable_path="chromedriver.exe")

    driver = webdriver.Chrome(service=service)

    # navigate to the app url
    driver.get("https://ebay.com")

    # time delay
    time.sleep(2)

    # maximize the window
    driver.maximize_window()

    driver.find_element(By.ID, "gh-ac").send_keys("We the Living");
    time.sleep(2)

    driver.find_element(By.ID, "gh-search-btn").click()

    assert driver.current_url == 'https://www.ebay.com/sch/i.html?_nkw=We+the+Living&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313'

    # to close the window
    driver.close()

    '''

    Script --> Client library --> ChromeDriver --> Browser


    '''