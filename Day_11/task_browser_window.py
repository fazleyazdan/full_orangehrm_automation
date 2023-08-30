from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://testautomationpractice.blogspot.com/')

inputData = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
inputData.send_keys('selenium')

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.implicitly_wait(5)  # for handling synchronization errors

# capture all links and loop through it so that we can click on each link and capture the browser window IDs
allChild = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//child::*//a")
for child in allChild:
    child.click()

allWindowIDs = driver.window_handles  # capture all browser windows IDs
for winIDs in allWindowIDs:
    driver.switch_to.window(winIDs)
    print(driver.title)

driver.quit()  # quit all browser windows at once
