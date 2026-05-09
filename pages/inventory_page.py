from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    FIRST_ADD_TO_CART = (
        By.XPATH,
        "(//button[contains(text(),'Add to cart')])[1]"
    )

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_item(self):
        self.click(self.FIRST_ADD_TO_CART)

    def get_cart_badge(self):
        return self.get_text(self.CART_BADGE)