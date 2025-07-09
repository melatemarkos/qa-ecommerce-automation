from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is the parent of all pages """
''' It contains all generic methods and utilities for all the pages'''

# BasePage provides shared utility methods for all page classes
class BasePage:
    def __init__(self,driver):
        self.driver = driver # Store WebDriver instance

    # Click on an element after waiting for it to be clickable
    def do_click(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

     # Type text into an input field after waiting for it to be visible
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(by_locator)  # not _all_elements
        ).send_keys(text)

    # Return text of a visible element
    # Placeholder for future use: fetch visible text from an element
    # ------- NOT BEING USED -----------#
    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

     # Check if an element is visible on the page
    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    # Wait until the page title matches the expected, then return it
    def get_title(self,title):
        print("Expected:", title)
        print("Actual:", self.driver.title)
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title