from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_add_to_cart(driver):
    LoginPage(driver).login(test_data.VALID_USER, test_data.VALID_PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_first_item()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert inventory.get_cart_count() == "1"