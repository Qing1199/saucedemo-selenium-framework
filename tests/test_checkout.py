from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils import test_data


def test_checkout(driver):

    # LOGIN
    login = LoginPage(driver)

    login.login(
        test_data.VALID_USER,
        test_data.VALID_PASSWORD
    )

    login.wait_url_contains("inventory")

    # ADD ITEM
    inventory = InventoryPage(driver)
    inventory.add_first_item()

    # CART
    cart = CartPage(driver)
    cart.go_to_cart()
    cart.click_checkout()

    # CHECKOUT
    checkout = CheckoutPage(driver)

    checkout.fill_info(
        test_data.FIRST_NAME,
        test_data.LAST_NAME,
        test_data.ZIP_CODE
    )

    checkout.continue_checkout()
    checkout.finish_checkout()

    # ASSERT
    success_message = checkout.get_success_message()

    assert "thank you" in success_message.lower()