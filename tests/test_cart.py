from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils import test_data


def test_go_to_cart(driver):

    login = LoginPage(driver)

    login.login(
        test_data.VALID_USER,
        test_data.VALID_PASSWORD
    )

    inventory = InventoryPage(driver)
    inventory.add_first_item()

    cart = CartPage(driver)
    cart.go_to_cart()

    assert "cart" in driver.current_url