from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

# Environment Setup
# Service is the location of chrome driver

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# visiting website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# used implicit wait so that the website can properly load and then the driver perform other actions
driver.implicitly_wait(7)

# finding the username and password field using XPATH
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')

# find element using class name
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

# find the total number of elements with same tag on a web page

str_elements = driver.find_elements(By.TAG_NAME, 'a')
print(len(str_elements))

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()  # click PIM


# find multiple elements with same class name and printing their length

store_elements = driver.find_elements(By.CLASS_NAME, 'oxd-topbar-body-nav-tab')
print(len(store_elements))

driver.close()


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
