from pages.login_page import LoginPage
from utils import test_data


def test_valid_login(driver):

    login = LoginPage(driver)

    login.login(
        test_data.VALID_USER,
        test_data.VALID_PASSWORD
    )

    login.wait_url_contains("inventory")

    assert "inventory" in driver.current_url

def test_invalid_login(driver):

    login = LoginPage(driver)

    login.login(
        test_data.INVALID_USER,
        test_data.INVALID_PASSWORD
    )

    error_message = login.get_error()

    assert "do not match" in error_message.lower()