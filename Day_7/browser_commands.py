import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# visiting website
driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')

# browser and application commands are different
# browser commands can be used when the browser opens and app commands work on the application in browser

# browser commands
# close()
# quit()

# when you open a browser a process is created in the background/backend
# the main difference bw close and quit
# when you use close() it closes the browser but does not kill the process and is still running
# the quit() commands close the browser as well as kill the process
# second difference is close() only closes one browser window i.e the parent window (the web url we want to visit)
# while quit() closes all the browser windows i.e the parent as well as the child windows
# (the link which we click which open other tabs/windows. quit closes them all)

driver.find_element(By.LINK_TEXT, 'Twitter').click()
# as the close commands closes the browser very quickly, so I used the sleep command to observe it
time.sleep(4)
driver.close()
# driver.quit()