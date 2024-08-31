from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage


class MenuPage(BasePage):
    MENU_OPEN_BUTTON = (By.CLASS_NAME, "bm-burger-button")
    MENU_CLOSE_BUTTON = (By.CLASS_NAME, "bm-cross-button")
    MENU_ITEM_LIST = (By.CLASS_NAME, "bm-item-list")
    MENU_ITEM = (By.CLASS_NAME, "menu-item")
    MENU_ITEM_LOGOUT = (By.ID, "logout_sidebar_link")
    MENU_ITEM_ALL_ITEMS = (By.ID, "inventory_sidebar_link")

    def open_menu(self) -> None:
        """Opens the menu and waits for it to be visible."""
        self.find_element(self.MENU_OPEN_BUTTON).click()
        self.wait_for_element_to_be_visible(self.MENU_ITEM_LIST)

    def close_menu(self) -> None:
        """Closes the menu and waits for it to be invisible."""
        self.find_element(self.MENU_CLOSE_BUTTON).click()
        self.wait_for_element_to_be_invisible(self.MENU_ITEM_LIST)

    def get_menu(self) -> WebElement:
        """Returns the menu element."""
        return self.find_element(self.MENU_ITEM_LIST)

    def get_menu_items(self) -> list[WebElement]:
        """Returns a list of menu item elements."""
        return self.find_elements(self.MENU_ITEM)

    def logout(self) -> None:
        """Clicks the logout button."""
        self.find_element(self.MENU_ITEM_LOGOUT).click()

    def go_to_all_items(self) -> None:
        """Clicks the 'All Items' link in the menu."""
        self.find_element(self.MENU_ITEM_ALL_ITEMS).click()