import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(3)

rows_count = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))

print('total no of rows: ', rows_count)

count = 0
for r in range(2, rows_count+1):
    price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
    if price <= '300':
        count += 1

print("books having price equal to 300: ", count)
print("books having price greater than 300: ", rows_count-count)

time.sleep(3)
driver.close()

