from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

# Service is the location of chrome driver

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# Environment Setup
# os.environ['PATH'] += r"C:\Drivers\chromedriver_win32"

# visiting website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# used implicit wait so that the website can properly load and then the driver perform other actions
driver.implicitly_wait(5)

# finding the username and password field using XPATH (this is Absolute/full XPATH)
# Ab.XPATH uses nodes and tags only
# (Ab.XPATH start from root node ie /Html) ((starts with /)

driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')

# find element using class name
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

# this is Relative/Partial XPATH (starts with //)
# Rel.XPATH must contain an Attribute
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()

# find element using LinkText
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()

# after login matching the title of the website
exp_title = driver.title
act_title = 'OrangeHRM'
if exp_title == act_title:
    print("test case passed!")
else:
    print("test case failed!")
driver.close()
# my_element = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")

