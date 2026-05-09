from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    ADD_TO_CART_BTN = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_item(self):
        self.click(*self.ADD_TO_CART_BTN)

    def get_cart_count(self):
        return self.find(*self.CART_BADGE).text