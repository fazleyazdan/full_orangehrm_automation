from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Environment Setup
os.environ['PATH'] += r"C:\Drivers\chromedriver_win32"
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager(version="114.0.5735.90").install()))

# visiting website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# used implicit wait so that the website can properly load and then the driver perform other actions
driver.implicitly_wait(7)

# finding the username and password field using XPATH
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')


# find element using class name
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

# this is Relative/Partial XPATH (starts with //)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()  # click config

# find element using LinkText
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# find element using partial LinkTest
# driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()

driver.close()
# my_element = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
