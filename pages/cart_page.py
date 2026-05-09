from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def go_to_cart(self):
        self.click(self.CART_ICON)
        self.wait_url_contains("cart")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_url_contains("checkout-step-one")