# test_add_to_cart.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.add_to_cart
def test_add_to_cart():
    # --- Setup Chrome driver ---
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)  # increased wait for reliability

    try:
        # --- Open site ---
        driver.get("https://www.saucedemo.com")

        # --- Login ---
        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # --- Add item to cart ---
        add_to_cart_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_btn.click()

        # --- Small delay to ensure badge appears ---
        time.sleep(1)

        # --- Verify cart badge ---
        cart_badge = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert cart_badge.text == "1", "Cart badge should show 1 item"

        print("Test passed: Item successfully added to cart.")

    except Exception as e:
        print(f" Test failed: {e}")
        raise e

    finally:
        driver.quit()
