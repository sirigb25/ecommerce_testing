import pytest
import allure

@allure.title("Verify addition works")
def test_addition():
    assert 2 + 3 == 5

@allure.title("Verify subtraction works")
def test_subtraction():
    assert 5 - 2 == 3
