# test_e2e_flow.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_e2e_checkout(driver):
    driver.get("https://www.saucedemo.com")

    wait = WebDriverWait(driver, 15)

    # --- LOGIN ---
    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # --- ADD MULTIPLE ITEMS TO CART ---
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light"
    ]
    for item_id in items_to_add:
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, item_id)))
        add_btn.click()

    # --- GO TO CART ---
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # --- CHECKOUT ---
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # --- FILL CHECKOUT INFO ---
    first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")
    continue_btn = driver.find_element(By.ID, "continue")

    first_name.send_keys("John")
    last_name.send_keys("Doe")
    postal_code.send_keys("12345")
    continue_btn.click()

    # --- FINISH ORDER ---
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()

    # --- VERIFY ORDER COMPLETE ---
    complete_header = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert "Thank you for your order!" in complete_header.text
