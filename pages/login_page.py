from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        username_input = self.find_element(self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self) -> object:
        return self.find_element(self.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
