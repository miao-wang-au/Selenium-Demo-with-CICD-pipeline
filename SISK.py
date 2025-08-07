import time
from datetime import date

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Think about how to implement @fixture by utilizing pytest
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")

driver.find_element(By.NAME, "username").send_keys("f4fadmin@f4f.com")
driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB")

# XPATH -> //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -> tagname[attribute='value'] -> //input[type='submit']

driver.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@data-testid='selectSupplier13']"))
)
driver.find_element(By.XPATH, "//button[@data-testid='selectSupplier13']").click()

WebDriverWait(driver, 5)

# button = driver.find_element(By.XPATH, "//button[@data-testid='button']")
# driver.execute_script("arguments[0].click();", button)


driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click() # The only way that has worked so far

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@title='Open']"))
)

driver.find_element(By.XPATH, "//button[@title='Open']").click()

# Click dropdown 'mater Private Hospital'
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]"))
)
driver.find_element(By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]").click()

############################################################################################


# Click button 'Create Requisition Order'
driver.find_element(By.XPATH, "//*[contains(text(), 'Create Requisition Order')]").click()

# Click Select Cost Center dropdown
WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.XPATH, "(//button[@title='Open'])[2]"))
)
driver.find_element(By.XPATH, "(//button[@title='Open'])[2]").click()

driver.find_element(By.XPATH, "//*[contains(text(), 'code3')]").click()

driver.find_element(By.ID, "consignment-invoice").click()

driver.find_element(By.XPATH, "//button[@data-testid='tab-1']").click()

driver.find_element(By.ID, "dropdown-field-id-0-0").send_keys("430003S")

WebDriverWait(driver, 15).until(
     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '430003S')]"))
)

driver.find_element(By.XPATH, "//*[contains(text(), '430003S')]").click()

driver.find_element(By.ID, "select-id-0-2").click()

driver.find_element(By.XPATH, "//option[@data-testid='options-0-2-1']").click()

driver.find_element(By.CSS_SELECTOR, "#text-field-id-0-4").send_keys("{}".format(date.today()))

driver.find_element(By.CSS_SELECTOR, "#submitButton").click()

driver.find_element(By.XPATH, "(//button[@type='button'])[14]").click()

driver.find_element(By.XPATH, "//input[@type='password']").send_keys("1234")


WebDriverWait(driver, 7).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "svg[data-testid='valid-pin-check']"))
)


driver.find_element(By.XPATH, "(//button[@type='button'])[16]").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "(//div[@role='alert'])[1]"))
)

requisitioncreated = driver.find_element(By.XPATH, "(//div[@role='alert'])[1]").text

print(requisitioncreated)


time.sleep(5)
