from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)


# Navigational commands  [ back (), forward (), refresh () ]
# it allows us to navigate and switch bw different sites
# navigational arrows can be seen in chrome. they are on the left side where we type the url

# now I want to visit this site
driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')

# after visiting, I want to visit another site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# now if I want to visit the first site. So I don't need to write it again
# as the browser remembers it, so instead I will use navigational commands
driver.back()  # navigate to nopcommerce
driver.forward()  # navigate to orangehrm
driver.refresh()  # refreshes the pages
driver.quit()