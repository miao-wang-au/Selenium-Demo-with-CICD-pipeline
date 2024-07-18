import time
from UserLogin import Login
from Add3Items import AddThreeItems
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.set_window_position(2000, 0)
driver.maximize_window()
driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")

Login("Hospital Theater", driver)

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Stock Levels')]"))
)

driver.find_element(By.XPATH, "//*[contains(text(), 'Stock Levels')]").click()

driver.find_element(By.LINK_TEXT, "Consignment").click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[6]/td[4]"))
)

StockScan = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]").text  # Check No. of item 430005S before scan
StockManual = driver.find_element(By.XPATH, "//tbody/tr[5]/td[4]").text  # Check No. of item 430004S before manual
StockSearch = driver.find_element(By.XPATH, "//tbody/tr[6]/td[4]").text  # Check No. of item 430003S before search

print("Number of stock for 430005S before being released: " + StockScan + "\n" +
      "Number of stock for 430004S before being released: " + StockManual + "\n" +
      "Number of stock for 430003S before being released: " + StockSearch)

###############################################################################################

driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]").click()

AddThreeItems(driver)
# # Click button 'Create Requisition Order'
# driver.find_element(By.XPATH, "//*[contains(text(), 'Create Requisition Order')]").click()
#
# # Click Select Cost Center dropdown
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, "(//button[@title='Open'])[2]"))
# )
# driver.find_element(By.XPATH, "(//button[@title='Open'])[2]").click()
#
# driver.find_element(By.XPATH, "//*[contains(text(), 'code3')]").click()
#
# driver.find_element(By.ID, "consignment-invoice").click()
#
# driver.find_element(By.XPATH, "//button[@data-testid='tab-1']").click()
#
# driver.find_element(By.ID, "dropdown-field-id-0-0").send_keys("430003S")
#
# WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '430003S')]"))
# )
#
# driver.find_element(By.XPATH, "//*[contains(text(), '430003S')]").click()
#
# driver.find_element(By.ID, "select-id-0-2").click()
#
# driver.find_element(By.XPATH, "//option[@data-testid='options-0-2-1']").click()
#
# driver.find_element(By.CSS_SELECTOR, "#text-field-id-0-4").send_keys(
#     "{}".format("{}".format(datetime.now().strftime("%d-%m-%Y-%H%M%S"))))
#
# driver.find_element(By.CSS_SELECTOR, "#submitButton").click()
#
# driver.find_element(By.XPATH, "(//button[@type='button'])[14]").click()
#
# driver.find_element(By.XPATH, "//input[@type='password']").send_keys("1234")
#
# WebDriverWait(driver, 7).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "svg[data-testid='valid-pin-check']"))
# )
#
# driver.find_element(By.XPATH, "(//button[@type='button'])[16]").click()
#
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@role='alert'])[1]"))
)

RequisitionCreated = driver.find_element(By.XPATH, "(//div[@role='alert'])[1]").text

print(RequisitionCreated)

driver.find_element(By.XPATH, "(//button[@title='Account settings'])[1]").click()
driver.find_element(By.XPATH, "(//li[normalize-space()='Logout'])[1]").click()

###############################################################################

Login("Customer Service", driver)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Requisitions"))
)

driver.find_element(By.LINK_TEXT, "Requisitions").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[10]"))
)

driver.find_element(By.XPATH, "(//button[@type='button'])[10]").click()

# click on the Release button
WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '(//button[contains(@class, "MuiButton-containedPrimary") '
                                          'and normalize-space()="Release"])[3]'))
)

driver.find_element(By.XPATH, '(//button[contains(@class, "MuiButton-containedPrimary") '
                              'and normalize-space()="Release"])[3]').click()

# wait for the pop-up success message
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]"))
)

releasemessage = driver.find_element(By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]").text

print(releasemessage)
##################################################################################################
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-9'])[2]"))
)

time.sleep(5)

driver.find_element(By.XPATH, "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-9'])[2]").click()

driver.find_element(By.LINK_TEXT, "Consignment").click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[6]/td[4]"))
)

StockScanReleased = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]").text  # Check No. of item 430005S by scan
StockManualReleased = driver.find_element(By.XPATH, "//tbody/tr[5]/td[4]").text  # Check No. of item 430004S by manual
StockSearchReleased = driver.find_element(By.XPATH, "//tbody/tr[6]/td[4]").text  # Check No. of item 430003S by search

print("Number of stock for 430005S after being released: " + StockScanReleased + "\n"
      "Number of stock for 430004S after being released: " + StockManualReleased + "\n"
      "Number of stock for 430003S after being released: " + StockSearchReleased)

assert "1" in "{}".format(int(StockScan) - int(StockScanReleased))
assert "0" in "{}".format(int(StockManual) - int(StockManualReleased))
assert "1" in "{}".format(int(StockSearch) - int(StockSearchReleased))

print("Regression Scenario 1 before CD message Successfully Executed")
