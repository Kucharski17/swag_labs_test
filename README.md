# Swag Labs Test Suite

## Overview

This project provides a comprehensive test suite for validating the functionality of a web application, focusing on the login and inventory pages. The tests are written in Python using the pytest framework and cover various scenarios, ensuring that both the login and inventory functionalities work as expected.

## Project Structure

- **test_login_page.py**: Contains test cases for validating the login functionality.
- **test_inventory_page.py**: Contains test cases for validating the inventory page functionality.
- **pages/login_page.py**: Defines the `LoginPage` class, encapsulating actions and queries related to the login page.
- **pages/inventory_page.py**: Defines the `InventoryPage` class, encapsulating actions and queries related to the inventory page.
- **conftest.py**: Provides shared fixtures for setting up and tearing down the browser driver, logging in users, and managing cart operations.

## Test Suites

### Login Page Test Cases

1. **test_valid_login**
   - **Purpose**: Ensures successful login with valid credentials.
   - **Steps**:
     1. Navigate to the login page.
     2. Enter a valid username ("standard_user") and password ("secret_sauce").
     3. Submit the login form.
   - **Assertion**: The user is redirected to the inventory page, verified by checking that the current URL contains "inventory".

2. **test_not_valid_login**
   - **Purpose**: Verifies that an error message is displayed when a user attempts to log in with an invalid password.
   - **Steps**:
     1. Navigate to the login page.
     2. Enter a valid username ("standard_user") and an invalid password ("some_wrong_password").
     3. Submit the login form.
   - **Assertion**: The error message "Username and password do not match any user in this service" is displayed.

3. **test_username_not_passed**
   - **Purpose**: Ensures that an error message is displayed when attempting to log in without providing a username.
   - **Steps**:
     1. Navigate to the login page.
     2. Leave the username field empty and enter a password ("some_password").
     3. Submit the login form.
   - **Assertion**: The error message "Epic sadface: Username is required" is displayed.

4. **test_not_valid_password**
   - **Purpose**: Ensures that an error message is displayed when attempting to log in without providing a password.
   - **Steps**:
     1. Navigate to the login page.
     2. Enter a valid username ("standard_user") and leave the password field empty.
     3. Submit the login form.
   - **Assertion**: The error message "Epic sadface: Password is required" is displayed.

### Inventory Page Test Cases

1. **test_is_inventory_displayed**
   - **Purpose**: Ensures that the inventory page displays a list of items.
   - **Assertion**: The list of inventory items is not empty.

2. **test_inventory_items_have_title_desc_price**
   - **Purpose**: Verifies that each item in the inventory has a title, description, and price.
   - **Assertion**: Every item has a non-empty title, description, and price.

3. **test_inventory_prices_are_positive**
   - **Purpose**: Checks that all inventory items have positive prices.
   - **Assertion**: Each item's price is greater than zero.

4. **test_inventory_prices_low_to_high**
   - **Purpose**: Validates that the inventory items are sorted correctly by price in ascending order.
   - **Assertion**: The list of prices is sorted from low to high.

5. **test_inventory_prices_high_to_low**
   - **Purpose**: Validates that the inventory items are sorted correctly by price in descending order.
   - **Assertion**: The list of prices is sorted from high to low.

6. **test_inventory_name_a_to_z**
   - **Purpose**: Verifies that the inventory items are sorted alphabetically from A to Z by their names.
   - **Assertion**: The list of names is sorted in ascending alphabetical order.

7. **test_inventory_name_z_to_a**
   - **Purpose**: Verifies that the inventory items are sorted alphabetically from Z to A by their names.
   - **Assertion**: The list of names is sorted in descending alphabetical order.

8. **test_inventory_add_to_cart**
   - **Purpose**: Tests adding an item to the cart.
   - **Assertion**: The number of items in the shopping cart increases by one after adding an item.

9. **test_inventory_change_button_after_add_to_cart**
   - **Purpose**: Checks if the inventory button text changes to "REMOVE" after adding an item to the cart.
   - **Assertion**: The button text for the added item changes to "REMOVE".

10. **test_inventory_remove_item_from_cart**
    - **Purpose**: Tests removing an item from the cart.
    - **Assertion**: The number of items in the shopping cart decreases by one after removing an item.

11. **test_inventory_change_after_remove_button**
    - **Purpose**: Ensures that the button text changes back to "ADD TO CART" after removing an item from the cart.
    - **Assertion**: The button text returns to "ADD TO CART" after the item is removed from the cart.

## How to Run the Tests

1. **Install dependencies**: Ensure that all required packages are installed. You can install them using pip:

   ```bash
   pip install -r requirements.txt

2. **Run the tests**: You can run all tests using the following command in the root folder of the project
   ```bash
   pytest
   
3. **View results**: The test results will be displayed in the console, showing passed and failed tests along with any assertion errors.   

## Additional Notes
- Ensure that the web application is running and accessible before running the tests.
- The tests are written with the assumption of a Selenium WebDriver setup in the conftest.py file. Make sure the driver is properly configured.