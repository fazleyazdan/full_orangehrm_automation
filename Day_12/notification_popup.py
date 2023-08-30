# notification popup/alert automation:
# notification popup does not come from an application or website it comes from the browser.
# for example: we visit a website and it want our location to allow it to proceed further.
# we can't bypass it or inject anything.
# switch_to.alert() won't work either to handle these kinds of notifications.
# the only way to disable it is, by using making a 'ChromeOptions()' object.
# we will add an argument to this object and pass it a value to disable it.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')  # for disabling notifications.
options.add_experimental_option("detach", True)  # for disabling the automatic closure of Chrome browser

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://whatmylocation.com/')