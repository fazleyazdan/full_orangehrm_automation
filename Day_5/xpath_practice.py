# in this practice I will use different methods used with XPATH

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
driver.implicitly_wait(3)

# using 'or' operator with XPATH
driver.find_element(By.XPATH, '//*[@name="username" or @placeholder="Username"]').send_keys('Admin')

# using 'and' operator with XPATH
driver.find_element(By.XPATH, '//*[@name="password" and @placeholder="Password"]').send_keys('admin123')

# contains() method with XPATH
# (Note: it is not necessary to use full form of the value with XPATH methods you can use half form of the word as well)
# for example: type,submit we can use this as well (type, subm)
# both the methods take two arguments

driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()

# starts-with() method used with XPATH
# driver.find_element(By.XPATH, '//button[starts-with(@type, "subm")]').click()

# using text() method with XPATH (it finds element based on the inner text)
# driver.find_element(By.XPATH, '//button[text()=" Login "]').click()
