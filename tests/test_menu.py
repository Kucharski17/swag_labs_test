import pytest
from pages.menu_page import MenuPage
from conftest import driver, log_user


@pytest.fixture
def logged_in_page_with_menu(driver):
    log_user(driver)
    return MenuPage(driver)


def open_menu_and_get_elements(logged_in_page_with_menu):
    logged_in_page_with_menu.open_menu()
    menu = logged_in_page_with_menu.get_menu()
    return menu, logged_in_page_with_menu.get_menu_items()


def test_is_menu_displayed_after_click_menu_button(logged_in_page_with_menu):
    menu, _ = open_menu_and_get_elements(logged_in_page_with_menu)
    assert menu.is_displayed(), "Menu should be displayed after clicking the menu button."


def test_is_menu_closed_after_click_close_menu_button(logged_in_page_with_menu):
    menu, _ = open_menu_and_get_elements(logged_in_page_with_menu)
    logged_in_page_with_menu.close_menu()
    assert not menu.is_displayed(), "Menu should not be displayed after clicking the close button."


def test_is_any_menu_item_present(logged_in_page_with_menu):
    _, menu_items = open_menu_and_get_elements(logged_in_page_with_menu)
    assert len(menu_items) > 0, "There should be at least one menu item."


def test_go_to_index_after_click_logout(logged_in_page_with_menu, driver):
    logged_in_page_with_menu.open_menu()
    logged_in_page_with_menu.logout()
    assert "/v1/index.html" in driver.current_url, "URL should contain '/v1/index.html' after logout."


def test_go_to_inventory_after_click_all_items(logged_in_page_with_menu, driver):
    logged_in_page_with_menu.open_menu()
    logged_in_page_with_menu.go_to_all_items()
    assert "/v1/inventory.html" in driver.current_url, \
        "URL should contain '/v1/inventory.html' after clicking 'All Items'."
