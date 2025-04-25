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
    driver.get('https://www.myntra.com')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()

def test_myntra_n(setup):
    driver.find_element(By.CSS_SELECTOR, "div> input.desktop-searchBar").send_keys("Bluetooth headphones")
    driver.find_element(By.XPATH,"//a[contains(@class, 'desktop-submit')]").click()

    element_search=driver.find_element(By.CSS_SELECTOR,"div>div.sort-sortBy")
    element_search.click()
    element_list = driver.find_element(By.CSS_SELECTOR, "span+span+ul>li:nth-child(2)")
    element_list.click()

    # driver.switch_to.alert.accept()
    # time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,"div.filter-search-filterSearchBox").click()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Brand']").send_keys("JBL")
    time.sleep(3)


    # driver.find_element(By.CSS_SELECTOR,"ul.brand-list>li:nth-child(6)>label>input[value='JBL']").click()
    # driver.find_element(By.CSS_SELECTOR, "ul.brand-list>label>input[value='JBL']").click()
    #driver.find_element(By.CSS_SELECTOR, "input[value='JBL']").click()
    element = driver.find_element(By.XPATH, "//ul[@class='brand-list']/li/label/input")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)

    dashboard_element = driver.find_element(By.TAG_NAME, "h3")

    assert dashboard_element.is_displayed() == True
    assert dashboard_element.text == 'JBL'





