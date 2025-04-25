import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import pytest

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture()
def setup():
    global driver
    driver.get('https://www.amazon.in')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()

def test_amazon(setup):
    driver.find_element(By.XPATH,"//label/following-sibling::input[@placeholder='Search Amazon.in']").send_keys("Bluetooth Speaker")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"span.nav-search-submit-text").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "span.a-dropdown-container").click()
    time.sleep(3)

    list_dropdown=driver.find_element(By.PARTIAL_LINK_TEXT,"Newest Arrivals")
    list_dropdown.click()
    time.sleep(3)

    categorylist = driver.find_elements(By.CSS_SELECTOR,"ul>li>a")
    for category in categorylist:
        print(category.text)

    asser = driver.find_element(By.CSS_SELECTOR, "span.a-color-base.a-text-bold")
    time.sleep(5)
    assert asser.is_displayed() == True
    assert asser.text == "12 - 14 May"

