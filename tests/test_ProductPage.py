import pytest

from pages.product_page import ProductPage
from config import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.test_base import BaseTest

class Test_Product(BaseTest):

    def test_verify_all_products(self):
        # Initialize the ProductPage with the active WebDriver
        self.productPage = ProductPage(self.driver)
        # Navigate to Product page
        self.productPage.go_to_product_page()
        # Assert "ALL PRODUCTS" headers is visible
        assert self.productPage.is_all_product_header_visible()

    def test_verify_all_products_details(self):
        # Initialize the ProductPage with the active WebDriver
        self.productPage = ProductPage(self.driver)
        # Click first "View Product" button
        self.productPage.view_first_product()
        # Wait for product details to appear
        self.productPage.wait_for_product_details()  # Wait for page to load
        # Click first "View Product" button
        assert self.productPage.are_product_details_displayed()