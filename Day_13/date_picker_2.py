from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='dob']").click()

month = 'december'
year = '2024'                   # expected values
date = '17'

# in this datepicker dropdown is available so we will use builtin 'Select' Class

dp_mon = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
dp_mon.select_by_visible_text('Aug')

dp_yr = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
dp_yr.select_by_visible_text('1997')

dp_date = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for ele in dp_date:
    if ele.text == date:
        ele.click()
        break


