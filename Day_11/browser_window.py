# switching between different browser windows
# to switch bw windows we will use driver.switch_to.window(). in the parenthesis we will pass the browser window id.
# now we can't see the window id in HTML dom. it is dynamic and is created when the browser window opens
# driver.current_window_handle : return windowID of single browser window
# driver.window_handles : return window ID's of multiple browsers windows
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

currentWindowId = driver.current_window_handle  # return id of the current window id
print(currentWindowId)
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()  # opens another browser window

allWindowIDs = driver.window_handles  # return IDs of all browser window in a list collection

# Approach 1:
# parentWindow = allWindowIDs[0]  # browser ID of the parent/main window
# childWindow = allWindowIDs[1]  # browser ID of the child window
# print(parentWindow, childWindow)
#
# driver.switch_to.window(childWindow)
# print('title of the child window: ', driver.title)
#
# driver.switch_to.window(parentWindow)
# print('title of the parent window: ', driver.title)

# Approach 2:
# the above approach is suitable for 2,3 browser windows. suppose there are 10 browser windows then we can't store title of every window
# for that we will use for loop to get the title of different windows
# print the title after switching to the other window

# print('printing title of windows using approach 2')
# for winId in allWindowIDs:
#     driver.switch_to.window(winId)
#     print(driver.title)

# closing specific browser window (all you need to do is to provide the title of that browser window)
time.sleep(3)
for winId in allWindowIDs:
    driver.switch_to.window(winId)
    if driver.title == 'OrangeHRM':
        driver.close()


