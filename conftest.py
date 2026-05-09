import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.config import BASE_URL

@pytest.fixture
def driver():

    chrome_options = Options()

    # Hide Chrome logs
    chrome_options.add_argument("--log-level=3")

    # Uncomment ONLY for CI/CD
    # Headless for CI
    chrome_options.add_argument("--headless=new")

    # Stability
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Disable password manager popup
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    service = Service()

    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    #driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()