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
    INVENTORY_ITEM_INVENTORY_BUTTON = (By.CLASS_NAME, "btn_inventory")
    INVENTORY_LIST_CART_COUNTER = (By.CLASS_NAME, 'shopping_cart_badge')

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

    def get_item_inventory_button(self, item):
        return item.find_element(*self.INVENTORY_ITEM_INVENTORY_BUTTON)

    def click_item_inventory_button(self, item):
        self.get_item_inventory_button(item).click()

    def get_item_shopping_cart_amount(self):
        try:
            cart_counter_text = self.find_element(self.INVENTORY_LIST_CART_COUNTER).text
            return int(cart_counter_text)
        except (NoSuchElementException, TimeoutException, ValueError):
            return 0

    def is_item_in_cart(self, item):
        return self.get_item_inventory_button(item).text == "REMOVE"

