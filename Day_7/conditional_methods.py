from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')

# conditional methods/commands
# is_displayed() used for checking the element is displayed on the web page or not
# is_enabled() means the element is enabled or not example : the input field enabled us to write in it or not
# is_selected() means the element is selected or not example : the checkbox or radio button

# These methods can only be used with web elements & cannot be accessed through 'driver'
# conditional commands are used for checking the status of the element on the web page.
# they are boolean and will return 'true' or 'false'

# is_displayed() is_enable()
search_box = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
print('display status: ', search_box.is_displayed())
print('enabled status: ', search_box.is_enabled())

# is_selected
rd_button = driver.find_element(By.XPATH, '//*[@id="gender-male"]')
print('selection status before clicking: ', rd_button.is_selected())

rd_button.click()
print('selection status after clicking: ', rd_button.is_selected())

driver.close()
