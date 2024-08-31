import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver() -> webdriver.Chrome:
    """
    Fixture to initialize the WebDriver for the tests.

    :return: An instance of the WebDriver.
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def log_user(driver: webdriver.Chrome, username: str = "standard_user", password: str = "secret_sauce") -> None:
    """
    Logs in a user with the given username and password.

    :param driver: The WebDriver instance used to interact with the browser.
    :param username: The username for login.
    :param password: The password for login.
    """
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login(username, password)
