# E-commerce Automation Testing Project

This project contains automated tests for a sample e-commerce website ([Sauce Demo](https://www.saucedemo.com)) using Selenium and Pytest.

Features Tested:

  Login – Verify valid user can log in successfully.  
  Add to Cart – Add a single or multiple items to the shopping cart.  
  Checkout – Complete checkout process including entering first name, last name, and postal code.  
  End-to-End Flow – Complete purchase flow from login to order confirmation.  
  Sample Tests – Additional example tests for arithmetic operations (used for practice).

  How to Run Tests:
1. Clone the repository
   
  git clone https://github.com/sirigb25/ecommerce_testing.git
   
2.Navigate to the project folder

  cd ecommerce_testing
  
3.Create a virtual environment 

  python -m venv venv

4.Activate the virtual environment

  Windows:
.\venv\Scripts\activate

5.Install dependencies

  pip install -r requirements.txt

6.Run tests using Pytest

  pytest -v

7.Clean and re-generate the report

allure generate allure-results -o allure-report --clean

8.Open the report

allure open allure-report
