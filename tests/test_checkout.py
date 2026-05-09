from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils import test_data

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_checkout(driver):

    wait = WebDriverWait(driver, 10)

    # LOGIN
    login = LoginPage(driver)
    login.login(test_data.VALID_USER, test_data.VALID_PASSWORD)

    wait.until(EC.url_contains("inventory"))

    # ADD ITEM
    inventory = InventoryPage(driver)
    inventory.add_first_item()

    # WAIT CART BADGE (IMPORTANT)
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    # GO TO CART
    cart = CartPage(driver)
    cart.go_to_cart()

    # WAIT CART PAGE
    wait.until(EC.url_contains("cart"))

    cart.click_checkout()

    # WAIT CHECKOUT PAGE
    wait.until(EC.url_contains("checkout-step-one"))

    # CHECKOUT INFO
    checkout = CheckoutPage(driver)
    checkout.fill_info(
        test_data.FIRST_NAME,
        test_data.LAST_NAME,
        test_data.ZIP_CODE
    )

    checkout.continue_checkout()

    # WAIT STEP 2
    wait.until(EC.url_contains("checkout-step-two"))

    checkout.finish_checkout()

    # WAIT SUCCESS
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    # ASSERT
    assert "thank you" in checkout.get_success_message().lower()