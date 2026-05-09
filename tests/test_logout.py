from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils import test_data


def test_logout(driver):

    login = LoginPage(driver)

    login.login(
        test_data.VALID_USER,
        test_data.VALID_PASSWORD
    )

    login.wait_url_contains("inventory")

    menu = MenuPage(driver)

    menu.logout()

    assert "saucedemo" in driver.current_url.lower()