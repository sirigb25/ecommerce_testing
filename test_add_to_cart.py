# test_add_to_cart.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com")

    wait = WebDriverWait(driver, 15)

    # --- LOGIN ---
    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # --- ADD TO CART ---
    add_to_cart_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_to_cart_btn.click()

    # --- VERIFY CART ---
    cart_badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert int(cart_badge.text) > 0, "Cart is empty!"
