from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils import test_data


def test_add_to_cart(driver):

    login = LoginPage(driver)

    login.login(
        test_data.VALID_USER,
        test_data.VALID_PASSWORD
    )

    login.wait_url_contains("inventory")

    inventory = InventoryPage(driver)

    inventory.add_first_item()

    badge = inventory.get_cart_badge()

    assert badge == "1"