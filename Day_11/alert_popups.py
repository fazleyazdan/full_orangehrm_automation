# alert and popups are not web elements, and we can't identify any element on the alert window

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')

# opens alert window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# you can use text() instead of normalize-space(). they are the same
# the only difference is that if there are additional spaces in the text it will be ignored
time.sleep(3)

alert_window = driver.switch_to.alert  # switch to alert window
# as we can't identify the alert window using locators so, we will use builtin methods
# print(alert_window.text)
alert_window.send_keys('my name is fazle yazdan')
alert_window.accept()  # close the alert window by clicking the 'ok' button. and we use it mostly
# alert_window.dismiss()  # close the alert window by clicking the cancel button

