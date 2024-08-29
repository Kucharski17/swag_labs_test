from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_LIST_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_ITEM_SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_primary")
    INVENTORY_LIST_CART_COUNTER = (By.CLASS_NAME, 'shopping_cart_badge')
    INVENTORY_ITEM_REMOVE_BUTTON = (By.CLASS_NAME, "btn_secondary")

    def get_inventory_items(self):
        return self.find_elements(self.INVENTORY_LIST_ITEMS)

    def get_item_title(self, item):
        return item.find_element(*self.INVENTORY_ITEM_NAME).text

    def get_item_desc(self, item):
        return item.find_element(*self.INVENTORY_ITEM_DESCRIPTION).text

    def get_item_price(self, item):
        price_text = item.find_element(*self.INVENTORY_ITEM_PRICE).text
        return float(price_text.replace("$", ""))

    def set_items_sort(self, text):
        select = Select(self.find_element(self.INVENTORY_ITEM_SORT_SELECT))
        select.select_by_visible_text(text)

    def click_item_add_to_cart_button(self, item):
        item.find_element(*self.INVENTORY_ITEM_ADD_TO_CART_BUTTON).click()

    def get_item_shopping_cart_amount(self):
        try:
            cart_counter_text = self.find_element(self.INVENTORY_LIST_CART_COUNTER).text
            return int(cart_counter_text)
        except (NoSuchElementException, TimeoutException, ValueError):
            return 0

    def get_remove_item_button(self, item):
        button = item.find_element(*self.INVENTORY_ITEM_REMOVE_BUTTON)
        return button

    def click_item_remove_from_cart(self, item):
        self.get_remove_item_button(item).click()

    def get_add_to_cart_item_button(self, item):
        button = item.find_element(*self.INVENTORY_ITEM_ADD_TO_CART_BUTTON)
        return button


