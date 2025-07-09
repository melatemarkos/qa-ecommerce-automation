from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import TestData

class ProductPage(BasePage):

    # Locators used on the Product page
    PRODUCT_LINK = (By.XPATH, "//a[contains(text(),'Products')]")
    ALL_PRODUCT_HEADER = (By.XPATH,"//h2[text()='All Products']")
    FIRST_VIEW_PRODUCT = (By.XPATH,"(//a[text()='View Product'])[1]")

    #Product details
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']/h2")
    PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']/p[contains(text(),'Category')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//div[@class='product-information']/p[b[text()='Availability:']]")
    PRODUCT_CONDITION = (By.XPATH, "//div[@class='product-information']/p[b[text()='Condition:']]")
    PRODUCT_BRAND = (By.XPATH, "//div[@class='product-information']/p[b[text()='Brand:']]")

    
    #------Constructor --------------#
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL) # Navigate to the homepage

    def go_to_product_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.PRODUCT_LINK)
            )
            self.do_click(self.PRODUCT_LINK)
        except TimeoutException:
            print("Products link was not clickable after waiting.")
            raise

    def is_all_product_header_visible(self):
        return self.is_visible(self.ALL_PRODUCT_HEADER)
    
    def view_first_product(self):
        self.do_click(self.FIRST_VIEW_PRODUCT)

    def are_product_details_displayed(self):
        return(
            self.is_visible(self.PRODUCT_NAME)
            and self.is_visible(self.PRODUCT_CATEGORY)
            and self.is_visible(self.PRODUCT_PRICE)
            and self.is_visible(self.PRODUCT_AVAILABILITY)
            and self.is_visible(self.PRODUCT_CONDITION)
            and self.is_visible(self.PRODUCT_BRAND)
        )
    
    def wait_for_product_details(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(self.PRODUCT_NAME)
    )