# links are web elements. there are 3 types of links
# 1: internal -- will navigate to the same page
# 2: external -- opens a new tab and will navigate to some other page
# 3: broken -- does not have any target page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://testautomationpractice.blogspot.com/')

# find the total no of links. we will find something which is common in all the links and, it is the tag name ie 'a'
links = driver.find_elements(By.TAG_NAME, 'a')
# links = driver.find_elements(By.XPATH, '//a')
print('total no of links: ', len(links))

# print all the link names
for link in links:
    print(link.text)