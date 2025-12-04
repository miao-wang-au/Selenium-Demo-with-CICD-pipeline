import os
import pytest
from selenium.webdriver.common.by import By


class TestLoginPage:

    def test_valid_login(self, driver):
        driver.get("https://www.saucedemo.com/")
        # time.sleep(2)

        # Type username
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")

        # Type password
        password_input = driver.find_element(By.ID, "password")
        valid_password = os.getenv("CORRECT_PASSWORD")  # <- read from GitHub secret
        password_input.send_keys(valid_password)

        # Click on the login button
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

        # URL Validation
        actual_url = driver.current_url
        assert actual_url == "https://www.saucedemo.com/inventory.html"

        # time.sleep(2)

    locked_password = os.getenv("CORRECT_PASSWORD")
    invalid_password = os.getenv("INVALID_PASSWORD")

    @pytest.mark.parametrize("username, password, error", [
        ("locked_out_user", locked_password, "Epic sadface: Sorry, this user has been locked out."),
        ("invalidUser", invalid_password, "Epic sadface: Username and password do not match any user in this service")])
    def test_invalid_login(self, driver, username, password, error):
        driver.get("https://www.saucedemo.com/")
        # time.sleep(2)

        # Type username
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys(username)

        # Type password
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        # Click on the login button
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

        # Error message validation
        error_msg_h3 = driver.find_element(By.TAG_NAME, "h3")
        error_msg_text = error_msg_h3.text
        assert error_msg_text == error

        # time.sleep(2)
