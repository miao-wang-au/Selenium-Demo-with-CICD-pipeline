import pytest
import os
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_create_requisition_order(driver):
    driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")

    driver.find_element(By.NAME, "username").send_keys("f4fadmin@f4f.com")
    sisk_password = os.getenv("SISK_PASSWORD")
    driver.find_element(By.NAME, "password").send_keys(sisk_password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-testid='selectSupplier13']"))
    ).click()

    driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Open']"))
    ).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]"))
    ).click()

    # Create Requisition Order
    driver.find_element(By.XPATH, "//*[contains(text(), 'Create Requisition Order')]").click()

    # Select Cost Center
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "(//button[@title='Open'])[2]"))
    ).click()

    driver.find_element(By.XPATH, "//*[contains(text(), 'code3')]").click()
    driver.find_element(By.ID, "consignment-invoice").click()
    driver.find_element(By.XPATH, "//button[@data-testid='tab-1']").click()

    driver.find_element(By.ID, "dropdown-field-id-0-0").send_keys("430003S")

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '430003S')]"))
    ).click()

    driver.find_element(By.ID, "select-id-0-2").click()
    driver.find_element(By.XPATH, "//option[@data-testid='options-0-2-1']").click()

    driver.find_element(By.CSS_SELECTOR, "#text-field-id-0-4").send_keys(str(date.today()))
    driver.find_element(By.CSS_SELECTOR, "#submitButton").click()

    driver.find_element(By.XPATH, "(//button[@type='button'])[14]").click()
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("1234")

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "svg[data-testid='valid-pin-check']"))
    )

    driver.find_element(By.XPATH, "(//button[@type='button'])[16]").click()

    alert_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@role='alert'])[1]"))
    ).text

    print(alert_text)
    assert "Requisition" in alert_text or alert_text != ""
