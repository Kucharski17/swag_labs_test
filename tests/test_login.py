from pages.login_page import LoginPage
from conftest import driver


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("standard_user", "secret_sauce")

    # Assertion: Checks if the user is redirected to the inventory page after a successful login
    assert "inventory" in driver.current_url


def test_not_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("standard_user", "some_wrong_password")
    error_message = login_page.get_error_message()

    # Assertion: Checks if the appropriate error message is displayed after a failed login attempt
    assert "Username and password do not match any user in this service" in error_message.text


def test_username_not_passed(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("",
                     "some_password")
    error_message = login_page.get_error_message()

    # Assertion: Checks if an error message is displayed when attempting to log in without providing a username
    assert "Epic sadface: Username is required" in error_message.text


def test_not_vailid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("standard_user",
                     "")
    error_message = login_page.get_error_message()

    # Assertion: Checks if an error message is displayed when attempting to log in without providing a password
    assert "Epic sadface: Password is required" in error_message.text
