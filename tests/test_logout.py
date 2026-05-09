from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils import test_data

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_logout(driver):

    # LOGIN
    login = LoginPage(driver)
    login.login(test_data.VALID_USER, test_data.VALID_PASSWORD)

    # LOGOUT
    menu = MenuPage(driver)
    menu.logout()

    # WAIT until login page appears again
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    # ASSERT
    assert "saucedemo" in driver.current_url