from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# in this task I will be using application commands and methods (also called webdriver commands)

# application commands

# get() -- get is a method used for opening a web page
# title -- used for getting the title of the web page
# current_url -- used for getting/capturing the current_url
# page_source -- used for getting the page source which is basically the HTML of the web page
# These commands and methods can only be used with 'driver' example: driver.get()

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()


