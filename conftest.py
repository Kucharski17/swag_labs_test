import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def login_user(driver, username, password):
    login_page = LoginPage(driver)
    login_page.go_to("/v1/index.html")
    login_page.login(username, password)
