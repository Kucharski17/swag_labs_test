from pages.login_page import LoginPage
from conftest import driver


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_not_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("standard_user", "some_wrong_password")
    error_message = login_page.get_error_message()

    assert "Username and password do not match any user in this service" in error_message


def test_username_not_passed(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("",
                     "some_password")
    error_message = login_page.get_error_message()

    assert "Epic sadface: Username is required" in error_message


def test_not_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login("standard_user",
                     "")
    error_message = login_page.get_error_message()

    assert "Epic sadface: Password is required" in error_message
