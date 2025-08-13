from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    # Set Chrome options (optional: headless mode for no browser pop-up)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment if you don’t want browser to open

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Step 1: Open site
    driver.get("https://www.saucedemo.com/")

    # Step 2: Enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Step 3: Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Step 4: Click login
    driver.find_element(By.ID, "login-button").click()

    # Step 5: Verify login worked
    assert "inventory" in driver.current_url

    driver.quit()
