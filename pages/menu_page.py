from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MenuPage(BasePage):

    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.click(*self.MENU_BTN)
        self.click(*self.LOGOUT)