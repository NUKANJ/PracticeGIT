import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pytest


def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.amazon.in")

    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(6) > div > a").click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "div>a:nth-child(6)").click()
    time.sleep(2)

    driver.find_element(By.PARTIAL_LINK_TEXT, 'Toys').click()
    time.sleep(4)

    # Locate the <h2> element that contains the word 'Results'
    h2_element = driver.find_element(By.XPATH, "//h2[contains(text(), 'Results')]")
    assert "Results" in h2_element.text, "Expected 'Results' in the <h2> element text"
    time.sleep(2)


    # Locate the <h2> element that contains the word 'Results'
    h2_element = driver.find_element(By.CSS_SELECTOR, "a > h2:nth-child(1)")
    assert "toy" in h2_element.text.lower(), "Expected 'watch' in the <h2> element"




