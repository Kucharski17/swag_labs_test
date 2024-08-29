import pytest
from pages.inventory_page import InventoryPage
from conftest import driver, log_user


@pytest.fixture
def logged_in_inventory_page(driver):
    log_user(driver)
    return InventoryPage(driver)


@pytest.fixture
def clear_cart(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page
    items = inventory_page.get_inventory_items()
    for item in items:
        if inventory_page.is_item_in_cart(item):
            inventory_page.click_item_inventory_button(item)
    yield
    # Clear the cart after the test to ensure isolation
    for item in items:
        if inventory_page.is_item_in_cart(item):
            inventory_page.click_item_inventory_button(item)


def test_is_inventory_displayed(logged_in_inventory_page):
    inventory_items = logged_in_inventory_page.get_inventory_items()
    assert len(inventory_items) > 0, "Inventory items list is empty"


def test_inventory_items_have_title_desc_price(logged_in_inventory_page):
    inventory_items = logged_in_inventory_page.get_inventory_items()
    for item in inventory_items:
        assert logged_in_inventory_page.get_item_title(item), "Title is missing for one of the inventory items"
        assert logged_in_inventory_page.get_item_desc(item), "Description is missing for one of the inventory items"
        assert logged_in_inventory_page.get_item_price(item), "Price is missing for one of the inventory items"


def test_inventory_prices_are_positive(logged_in_inventory_page):
    items = logged_in_inventory_page.get_inventory_items()
    for item in items:
        price = logged_in_inventory_page.get_item_price(item)
        assert price > 0, f"The price: {price} is not greater than zero for the product {logged_in_inventory_page.get_item_title(item)}"


def test_inventory_prices_low_to_high(logged_in_inventory_page):
    logged_in_inventory_page.set_items_sort("Price (low to high)")
    items = logged_in_inventory_page.get_inventory_items()
    prices = [logged_in_inventory_page.get_item_price(item) for item in items]
    assert prices == sorted(prices), "The product list is not sorted from lowest to highest price"


def test_inventory_prices_high_to_low(logged_in_inventory_page):
    logged_in_inventory_page.set_items_sort("Price (high to low)")
    items = logged_in_inventory_page.get_inventory_items()
    prices = [logged_in_inventory_page.get_item_price(item) for item in items]
    assert prices == sorted(prices, reverse=True), "The product list is not sorted from highest to lowest price"


def test_inventory_name_a_to_z(logged_in_inventory_page):
    logged_in_inventory_page.set_items_sort("Name (A to Z)")
    items = logged_in_inventory_page.get_inventory_items()
    names = [logged_in_inventory_page.get_item_title(item) for item in items]
    assert names == sorted(names), "The product list is not sorted alphabetically from A to Z"


def test_inventory_name_z_to_a(logged_in_inventory_page):
    logged_in_inventory_page.set_items_sort("Name (Z to A)")
    items = logged_in_inventory_page.get_inventory_items()
    names = [logged_in_inventory_page.get_item_title(item) for item in items]
    assert names == sorted(names, reverse=True), "The product list is not sorted alphabetically from Z to A"


def test_inventory_add_to_cart(logged_in_inventory_page, clear_cart):
    items = logged_in_inventory_page.get_inventory_items()
    logged_in_inventory_page.click_item_inventory_button(items[0])
    assert logged_in_inventory_page.get_item_shopping_cart_amount() == 1


def test_inventory_change_button_after_add_to_cart(logged_in_inventory_page, clear_cart):
    items = logged_in_inventory_page.get_inventory_items()
    sut = items[0]
    logged_in_inventory_page.click_item_inventory_button(sut)
    button = logged_in_inventory_page.get_item_inventory_button(sut)
    assert button.text == "REMOVE"


def test_inventory_remove_item_from_cart(logged_in_inventory_page, clear_cart):
    items = logged_in_inventory_page.get_inventory_items()
    sut = items[0]
    logged_in_inventory_page.click_item_inventory_button(sut)
    logged_in_inventory_page.click_item_inventory_button(sut)
    assert logged_in_inventory_page.get_item_shopping_cart_amount() == 0


def test_inventory_change_after_remove_button(logged_in_inventory_page, clear_cart):
    items = logged_in_inventory_page.get_inventory_items()
    sut = items[0]
    logged_in_inventory_page.click_item_inventory_button(sut)
    logged_in_inventory_page.click_item_inventory_button(sut)
    inventory_button = logged_in_inventory_page.get_item_inventory_button(sut)
    assert inventory_button.text == "ADD TO CART", "The button did not return to 'Add to Cart' after removing the item"
