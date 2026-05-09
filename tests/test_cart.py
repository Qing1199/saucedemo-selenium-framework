from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils import test_data

def test_add_to_cart(driver):
    LoginPage(driver).login(test_data.VALID_USER, test_data.VALID_PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_first_product()

    assert inventory.get_cart_count() == "1"