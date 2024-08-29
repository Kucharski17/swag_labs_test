from pages.inventory_page import InventoryPage
from conftest import driver, log_user


def logged_in_inventory_page(driver):
    log_user(driver)
    return InventoryPage(driver)


def clear_cart(driver):
    inventory_page = InventoryPage(driver)
    items = inventory_page.get_inventory_items()
    for item in items:
        if inventory_page.is_item_in_cart(item):
            inventory_page.click_item_inventory_button(item)


def test_is_inventory_displayed(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    inventory_items = inventory_page.get_inventory_items()

    # Assertion: Checks if the inventory product list is not empty
    assert len(inventory_items) > 0, "Inventory items list is empty"


def test_inventory_items_have_title_desc_price(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    inventory_items = inventory_page.get_inventory_items()

    for item in inventory_items:
        title = inventory_page.get_item_title(item)
        desc = inventory_page.get_item_desc(item)
        price = inventory_page.get_item_price(item)

        # Assertion: Checks if each item in the inventory has a title
        assert title, "Title is missing for one of the inventory items"

        # Assertion: Checks if each item in the inventory has a description
        assert desc, "Description is missing for one of the inventory items"

        # Assertion: Checks if each item in the inventory has a price
        assert price, "Price is missing for one of the inventory items"


def test_inventory_prices_are_positive(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    items = inventory_page.get_inventory_items()

    for item in items:
        price = inventory_page.get_item_price(item)

        # Assertion: Checks if the product price displayed on the page is greater than 0
        assert price > 0, f'''The price: price {price} is not greater then
        zero for the product {inventory_page.get_item_title(item)}'''


def test_inventory_prices_low_to_high(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    inventory_page.set_items_sort("Price (low to high)")
    items = inventory_page.get_inventory_items()
    prices = []

    for item in items:
        price = inventory_page.get_item_price(item)
        prices.append(price)

    # Assertion: Checks if the product list is sorted from lowest to highest price
    assert prices == sorted(prices), "The product list is not sorted from lowest to highest price"


def test_inventory_prices_high_to_low(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    inventory_page.set_items_sort("Price (high to low)")
    items = inventory_page.get_inventory_items()
    prices = []

    for item in items:
        price = inventory_page.get_item_price(item)
        prices.append(price)

    # Assertion: Checks if the product list is sorted from highest to lowest price
    assert prices == sorted(prices, reverse=True), "The product list is not sorted from highest to lowest price"


def test_inventory_name_a_to_z(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    inventory_page.set_items_sort("Name (A to Z)")
    items = inventory_page.get_inventory_items()
    names = []

    for item in items:
        name = inventory_page.get_item_title(item)
        names.append(name)

    # Assertion: Checks if the product list is sorted from A to Z
    assert names == sorted(names), "he product list is not sorted alphabetically from A to Z"


def test_inventory_name_z_to_a(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    inventory_page.set_items_sort("Name (Z to A)")
    items = inventory_page.get_inventory_items()
    names = []

    for item in items:
        name = inventory_page.get_item_title(item)
        names.append(name)

    # Assertion: Checks if the product list is sorted from Z to A
    assert names == sorted(names, reverse=True), "The product list is not sorted alphabetically from Z to A"


def test_inventory_add_to_cart(driver):
    log_user(driver)

    inventory_page = InventoryPage(driver)
    items = inventory_page.get_inventory_items()
    sut = items[0]

    inventory_page.click_item_inventory_button(sut)

    # Assertion: Checks if the number of items in the cart is 1 after adding the first product
    assert inventory_page.get_item_shopping_cart_amount() == 1


def test_inventory_change_button_after_add_to_card(driver):
    log_user(driver)

    clear_cart(driver)

    inventory_page = InventoryPage(driver)
    items = inventory_page.get_inventory_items()
    sut = items[0]

    inventory_page.click_item_inventory_button(sut)

    # Assertion: Checks if the button text for the first item has changed to "REMOVE"
    button = inventory_page.get_item_inventory_button(sut)
    assert button.text == "REMOVE"


def test_inventory_remove_item_from_card(driver):
    log_user(driver)

    clear_cart(driver)

    inventory_page = InventoryPage(driver)
    items = inventory_page.get_inventory_items()
    sut = items[0]

    inventory_page.click_item_inventory_button(sut)
    inventory_page.click_item_inventory_button(sut)

    assert inventory_page.get_item_shopping_cart_amount() == 0


def test_inventory_change_after_remove_button(driver):
    log_user(driver)

    clear_cart(driver)

    inventory_page = InventoryPage(driver)
    items = inventory_page.get_inventory_items()
    sut = items[0]

    inventory_page.click_item_inventory_button(sut)
    inventory_page.click_item_inventory_button(sut)
    inventory_button = inventory_page.get_item_inventory_button(sut)

    assert inventory_button.text == "ADD TO CART", ("The button did not return to 'Add to Cart' after removing the "
                                                    "item")
