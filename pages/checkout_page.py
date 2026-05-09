from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.ZIP_CODE, zip_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)
        self.wait_url_contains("checkout-step-two")

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)