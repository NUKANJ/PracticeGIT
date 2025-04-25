import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

def test_googletest():
    os.chdir("../lib")

    # Set up the ChromeDriver service
    service = Service(executable_path="chromedriver.exe")

    # Launch the browser using the service
    driver = webdriver.Chrome(service=service)

    # Navigate to the app url
    driver.get("https://google.com")

    # Wait for 5 seconds
    time.sleep(5)

    # Maximize the window
    driver.maximize_window()

    # Close the browser
    driver.close()
