import pytest
from requests import request
from config import TestData
from selenium import webdriver

# ChromeDriverManager automatically installs the right version of the ChromeDriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager #auto installs correct version

# Fixture to initialize and return the WebDriver instance
@pytest.fixture
def init_driver(request):
    # Setup: Start a Chrome browser session
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window() # Maximize browser for better visibility

    # Make driver accessible to test classes via `self.driver`
    request.cls.driver = driver  

    # Yield makes this a setup/teardown fixture: tests run after yield
    yield driver 
    
    # Teardown: Close the browser after the test is done
    driver.quit()