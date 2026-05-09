from pages.login_page import LoginPage
from utils import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_valid_login(driver):
    login = LoginPage(driver)
    login.login(test_data.VALID_USER, test_data.VALID_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.login(test_data.INVALID_USER, test_data.INVALID_PASSWORD)

    error_text = login.get_error().lower()

    assert "username and password do not match" in error_text