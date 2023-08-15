from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

# Environment Setup
ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# visiting website
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# used implicit wait so that the website can properly load and then the driver perform other actions
# driver.implicitly_wait(7)

# finding the username and password field using XPATH
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')

# find element using class name
# driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

# finding web elements using CSS SELECTORS
# tag name  and id (note : tag name is optional in css selectors)

driver.get("https://www.facebook.com/login/")
driver.implicitly_wait(5)
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('checking')

# As tag name is optional so this will also work (note : remember to use "#" with id)
# driver.find_element(By.CSS_SELECTOR, '.email').send_keys('checking')

# find element using tag name and class name
# if multiple elements have same CSS SELECTORS then the element matching first will be selected
# driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('checking')

# find element using tag name attribute
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email address or phone number"]').send_keys('checking')

# find element using tag name class and attribute
driver.find_element(By.CSS_SELECTOR, '.inputtext[placeholder="Email address or phone number"]').send_keys('checking')

