import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')

# Note : the web element is also called web element object
# you cannot print the web element object i.e print(element)
# because it contains multiple methods and properties and will give you an error
# instead we can use single method or return a property value of an object with web element objects i.e (element.text)
# in this case .text is a property of an 'element' object, and we are printing its value

# find_element returns single web element
# scenario 1: locator matches with 1 element web element
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys('Iphone')

# scenario 2: locator matches with multiple web element objects
# now this matches 23 'a' elements but will return only the first element since we are using findElement
element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(element.text)

# scenario 3: locator does not match any element on the web page (NoSuchElementException)
# element = driver.find_element(By.LINK_TEXT, "Log")
# element.click()

# find_elements returns multiple web elements
# find_elements always return web elements in a 'list' collection.
# 'list object' which is different from 'web element object'

# scenario 1: locator matches with 1 element web element
elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")

# now I cannot use this print(elements.text) and will give error because it is a list, so I need to specify the index
elements[0].send_keys('Samsung')

# scenario 2: locator matches with multiple elements
elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(elements))  # 23
print(elements[0].text)  # Sitemap

# if I want to print the elements of all texts I have to use the loops
for ele in elements:
    print(ele.text)

# scenario 3: locator matches with no elements
elements = driver.find_elements(By.LINK_TEXT, "Log")
print(len(elements))  # find_elements will not throw exception because there is no element in the list collection

elements = driver.find_elements(By.LINK_TEXT, "Log")
print(elements[0].text)  # will give an error list index out of range