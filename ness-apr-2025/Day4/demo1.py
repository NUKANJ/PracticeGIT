import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    
    driver.maximize_window()
    driver.implicitly_wait(15)

    #driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.XPATH, '//form/div[1]/div/div[2]/input').send_keys('Admin')
    time.sleep(2)

    #driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH, '//form/div[2]/div/div[2]/input').send_keys('admin123')
    time.sleep(2)

    #driver.find_element(By.TAG_NAME,"button").click()
    driver.find_element(By.TAG_NAME,"button").submit()

    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    dashboard_element = driver.find_element(By.TAG_NAME,"h6")

    assert dashboard_element.is_displayed() == True
    assert dashboard_element.text == 'Dashboard'

    driver.find_element(By.CLASS_NAME,'oxd-userdropdown-tab').click()
    time.sleep(2)

    #driver.find_element(By.LINK_TEXT,'Logout').click()
    driver.find_element(By.PARTIAL_LINK_TEXT,'logo').click()
    time.sleep(2)

    assert driver.title == "OrangeHRM"

    driver.close()