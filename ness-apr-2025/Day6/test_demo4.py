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
    driver.get('https://javascript.info/alert-prompt-confirm')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()

#@pytest.mark.skip
def test_simple_alert(setup):
    driver.find_element(By.CSS_SELECTOR,"div#rtel4ob7td div:nth-child(1)>a").click()
    time.sleep(2)
    assert driver.switch_to.alert.text == 'Hello'
    driver.switch_to.alert.accept()
    time.sleep(5)

@pytest.mark.skip
def test_confirm_alert(setup):
    driver.find_element(By.CSS_SELECTOR,'div#99wybcdk8d div:first-child > a').click()
    time.sleep(2)
    assert driver.switch_to.alert.text == 'Are you the boss?'
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)
    assert driver.switch_to.alert.text == 'false'
    driver.switch_to.alert.accept()
    time.sleep(2)

def test_prompt_alert(setup):
    driver.find_element(By.CSS_SELECTOR,'#wsxp6vv1wm div:nth-child(1) > a').click()
    time.sleep(2)
    driver.switch_to.alert.send_keys("29")
    time.sleep(4)
    driver.switch_to.alert.accept()
    time.sleep(4)
    driver.switch_to.alert.accept()