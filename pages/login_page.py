from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from typing import Optional


class LoginPage(BasePage):
    # Locators for elements on the login page
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username: str) -> None:
        """
        Enters the username into the username input field.

        :param username: The username to enter.
        """
        username_input = self.find_element(self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Enters the password into the password input field.

        :param password: The password to enter.
        """
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self) -> None:
        """
        Clicks the login button to submit the login form.
        """
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self) -> Optional[str]:
        """
        Retrieves the error message displayed on the login page.

        :return: The text of the error message if it exists, else None.
        """
        try:
            error_element = self.find_element(self.ERROR_MESSAGE)
            return error_element.text
        except NoSuchElementException:
            return None

    def login(self, username: str, password: str) -> None:
        """
        Performs the login action by entering the username, password, and clicking the login button.

        :param username: The username to enter.
        :param password: The password to enter.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
