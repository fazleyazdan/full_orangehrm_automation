# a.popups are not common and are only used inside the company or corporation
# they are not part of the app and is imposed on top of the app to authorize you before accessing it.
# there when you want to access there utilities on their app. most likely you will have to Log in via auth.popup
# the only you can automate this is to bypass this.
# we can bypass it by providing the username and password inside the url. this is also called injecting

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
# driver.get('https://the-internet.herokuapp.com/digest_auth')

# syntax : http:// username:password @ test.com
driver.get('https://admin:admin@the-internet.herokuapp.com/digest_auth')  # injecting

