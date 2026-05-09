from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
        self.wait_url_contains("saucedemo")