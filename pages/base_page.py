from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str = "https://www.saucedemo.com") -> None:
        """
        Initializes the BasePage with a WebDriver instance and an optional base URL.

        :param driver: The WebDriver instance used to interact with the browser.
        :param base_url: The base URL of the application under test.
        """
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Finds a single element on the page using the provided locator.

        :param locator: A tuple containing the method and value to locate the element (e.g., (By.ID, "element_id")).
        :param timeout: Maximum time to wait for the element to be present.
        :return: The WebElement found.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple[str, str], timeout: int = 10) -> list[WebElement]:
        """
        Finds multiple elements on the page using the provided locator.

        :param locator: A tuple containing the method and value to locate the elements (e.g., (By.CLASS_NAME,
        "class_name")).
        :param timeout: Maximum time to wait for the elements to be present.
        :return: A list of WebElements found.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def wait_for_element_to_be_visible(self, locator, timeout=1):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_invisible(self, locator, timeout=1):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def go_to(self, url: str = "") -> None:
        """
        Navigates to a specific URL by appending it to the base URL.

        :param url: The relative URL to navigate to.
        """
        self.driver.get(self.base_url + url)
