from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# this will prevent the browser from automatically closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.get('https://admin-demo.nopcommerce.com/login')

email_box = driver.find_element(By.XPATH, "//input[@id='Email']")

# It will clear the input field in case there is a placeholder or any text
email_box.clear()
email_box.send_keys('fazleyazdan345@gmail.com')

print('result with .text: ', email_box.text)
# this will print nothing as there is no innertext of this element
# .text only return innertext of an element
# .text only captures the text which is already there not the text we have send

# now in this case get_attribute() comes handy, and it captures the text we have sent to the 'value attribute'
# get_attribute() return the value of any attribute
print('result with get_attribute:', email_box.get_attribute('value'))


