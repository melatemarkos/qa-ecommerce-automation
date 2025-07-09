from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TestData

# Page object representing the Login page
class LoginPage(BasePage):

    # Locators used on the Login/Signup page
    LOGIN_SIGNUP_LINK = (By.LINK_TEXT, "Signup / Login")
    LOGIN_EMAIL =  (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASS = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']" )
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "input[data-qa='signup-button']")
    LOGIN_PAGE_HEADER = (By.XPATH, "//h2[text()='Login to your account']")

    #------Constructor --------------#
    def __init__(self, driver):
        # Initialize BasePage
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL) # Navigate to the homepage

    #------- Page Actions ----------- #

    #------Wanted to use this to check that login was visible on the screen after click link ---#
    # Get the page title and verify it matches
    # ------- NOT BEING USED -----------#
    def get_login_page_title(self,title):
        return self.get_title(title)
    
    # Check if Signup/Login link is visible 
    def is_signup_login_link_exist(self):
        return self.is_visible(self.LOGIN_SIGNUP_LINK)
    
    # Explicitly wait for login text to be visible in a header
    def wait_for_login_text(self):
        WebDriverWait(self.driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "h2"), "Login to your account")
        )
    
    # Full login action: click link, fill form, click login
    def do_login(self, email,password):
        self.do_click(self.LOGIN_SIGNUP_LINK)
        self.wait_for_login_text()
        self.do_send_keys(self.LOGIN_EMAIL,email)
        self.do_send_keys(self.LOGIN_PASS,password)
        self.do_click(self.LOGIN_BUTTON)
    
    # Navigate to login form
    def click_signup_login_link(self):
        self.do_click(self.LOGIN_SIGNUP_LINK)
    
    # Wait for form header to load
    def wait_for_login_form(self):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.LOGIN_PAGE_HEADER)
        )