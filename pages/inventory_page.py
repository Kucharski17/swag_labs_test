from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class InventoryPage(BasePage):
    # Locators for elements on the inventory page
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_LIST_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_ITEM_SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_INVENTORY_BUTTON = (By.CLASS_NAME, "btn_inventory")
    INVENTORY_LIST_CART_COUNTER = (By.CLASS_NAME, 'shopping_cart_badge')

    def get_inventory_items(self) -> list[WebElement]:
        """Returns a list of inventory items."""
        return self.find_elements(self.INVENTORY_LIST_ITEMS)

    def get_item_title(self, item) -> str:
        """Returns the title of the given item."""
        return item.find_element(*self.INVENTORY_ITEM_NAME).text

    def get_item_desc(self, item) -> str:
        """Returns the description of the given item."""
        return item.find_element(*self.INVENTORY_ITEM_DESCRIPTION).text

    def get_item_price(self, item) -> float:
        """Returns the price of the given item as a float."""
        price_text = item.find_element(*self.INVENTORY_ITEM_PRICE).text
        return float(price_text.replace("$", ""))

    def set_items_sort(self, text) -> None:
        """Selects sorting option from the dropdown."""
        select = Select(self.find_element(self.INVENTORY_ITEM_SORT_SELECT))
        select.select_by_visible_text(text)

    def get_item_inventory_button(self, item) -> WebElement:
        """Returns the inventory button element for the given item."""
        return item.find_element(*self.INVENTORY_ITEM_INVENTORY_BUTTON)

    def click_item_inventory_button(self, item) -> None:
        """Clicks the inventory button for the given item."""
        self.get_item_inventory_button(item).click()

    def click_item_add_to_cart_button(self, item) -> None:
        """Adds the item to the cart if it's not already in the cart."""
        if not self.is_item_in_cart(item):
            self.click_item_inventory_button(item)
        else:
            raise ValueError("Item is already in the cart!")

    def click_item_remove_from_cart_button(self, item) -> None:
        """Removes the item from the cart if it's currently in the cart."""
        if self.is_item_in_cart(item):
            self.click_item_inventory_button(item)
        else:
            raise ValueError("Item isn't in the cart!")

    def get_item_shopping_cart_amount(self) -> int:
        """Returns the number of items in the shopping cart."""
        try:
            cart_counter_text = self.find_element(self.INVENTORY_LIST_CART_COUNTER).text
            return int(cart_counter_text)
        except (NoSuchElementException, TimeoutException, ValueError) as e:
            return 0

    def is_item_in_cart(self, item) -> bool:
        """Checks if the item is currently in the cart by checking the button text."""
        return self.get_item_inventory_button(item).text == "REMOVE"

    def get_first_inventory_item(self) -> WebElement:
        """Returns the first item in the inventory list."""
        items = self.get_inventory_items()
        if not items:
            raise IndexError("No inventory items found.")
        return items[0]
