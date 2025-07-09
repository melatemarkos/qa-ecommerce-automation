import pytest

from pages.login_page import LoginPage
from config import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.test_base import BaseTest

# Test class for login functionality
class Test_Login(BaseTest):

    # --------------- POSITIVE LOGIN TEST --------------------------------#

    # Smoke test: make sure the homepage loads
    def test_open_home_page(self,init_driver):
        driver = init_driver
        driver.get("https://www.automationexercise.com/")
        assert "Automation Exercise" in driver.title
    
    # Check if the signup/login link exists
    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_login_link_exist()
        assert flag # expecting a true value
    
    # Validate the login page title
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_signup_login_link()
        self.loginPage.wait_for_login_form() 
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
    
    # Complete login process using credentials
    def test_login_valid_credentials(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.LOGIN_USERNAME,TestData.LOGIN_PASSWORD)

        # wait for and assert that user is logged in
        logged_in_text = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"//a[text()=' Logged in as ']"))
        )
        assert logged_in_text.is_displayed()
    
    #------------------- NEGATIVE LOGIN TEST ---------------------------------------#
    def test_login_invalid_credentials(self):
        """
        NEGATIVE TEST:
        Attempt to log in with invalid credentials and verify error message appears.
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("wrong@example.com","WrongPassword456")

        # wait for error message to appear
        error_message = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']"))
        )

        assert error_message.is_displayed()
        assert "incorrect" in error_message.text.lower()