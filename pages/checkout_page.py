from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    SUCCESS = (By.CLASS_NAME, "complete-header")

    def fill_info(self, fname, lname, zip):
        self.type(*self.FIRST_NAME, fname)
        self.type(*self.LAST_NAME, lname)
        self.type(*self.ZIP, zip)

    def continue_checkout(self):
        self.click(*self.CONTINUE)

    def finish_checkout(self):
        self.click(*self.FINISH)

    def get_success_message(self):
        return self.find(*self.SUCCESS).text