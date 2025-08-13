from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout():
    # --- Setup ---
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

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

        # --- Go to cart ---
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()

        # --- Checkout ---
        checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()

        # --- Enter user info ---
        first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        postal_code.send_keys("12345")

        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()

        # --- Finish checkout ---
        finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finish_btn.click()

        # --- Verify confirmation ---
        complete_header = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert complete_header.text.strip().lower() == "thank you for your order!"
        print("Checkout completed successfully!")

    finally:
        driver.quit()
