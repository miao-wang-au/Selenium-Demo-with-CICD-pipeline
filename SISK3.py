import pytest
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


def test_release_requisition(driver):
    # ---------------- Login ----------------
    driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")
    driver.find_element(By.NAME, "username").send_keys("f4fadmin@f4f.com")
    driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # ---------------- Select Supplier ----------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-testid='selectSupplier13']"))
    ).click()

    WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Open']"))
    ).click()

    # Select 'Mater Private Hospital'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]"))
    ).click()

    # ---------------- Navigate to Requisitions ----------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Requisitions"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(6) button:nth-child(2)"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[44]"))
    ).click()

    # ---------------- Wait for release message ----------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]"))
    )
    releasemessage = driver.find_element(By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]").text
    print(releasemessage)

    # Optional: assert message is not empty
    assert releasemessage != ""
