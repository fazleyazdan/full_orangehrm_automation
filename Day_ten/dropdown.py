import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://testautomationpractice.blogspot.com/')

# dropdown has tag name 'select'. and it is a single web element
# inside the select tag we have multiple tag names called 'options' which hold text or values

# first identify the dropdown and store it
dropdown_element = driver.find_element(By.XPATH, "//select[@id='country']")
# now we can't access the option directly in a dropdown so, we have to use the built_in select module in a package
# we will pass dropdown element to the select module in order to access its options.

# option_element = Select(driver.find_element(By.XPATH, "//select[@id='country']"))  # we can do this as well
# Note: select method is only for the 'select' tag.sometimes we have 'div' or some other tag for that we will use XPATH

opt_element = Select(dropdown_element)  # object of select class (use it for accessing option elements)
opt_element.select_by_visible_text('Canada')  # case Sensitive: provide exactly the same option text otherwise error
opt_element.select_by_value('usa')  # extra the value attribute value from HTML DOM and select the option via it
opt_element.select_by_index(3)  # select the value using index.you have to find the index manually.don't write it in db.commas as it is index number

# capture all the options and catch them. we have 2 approaches for that
# 1: write a common XPATH and capture option
# 2: use built in methode 'option' and capture all the option inside the dropdown
# you can use child::option , or you can just use /option and, it will select all the option
# capture_opt_xp = driver.find_elements(By.XPATH, "//select[@id='country']/child::option")
capture_opt_xp = driver.find_elements(By.XPATH, "//select[@id='country']/option")

for cop in capture_opt_xp:
    print(cop.text)

builtin_op = opt_element.options  # this will return all the option elements inside the dropdown
for cop in builtin_op:
    print(cop.text)

# time.sleep(3)
# if I want to print a specific option without using builtin function ie 'select_by_value' or select_by_index etc ...
for cop in capture_opt_xp:
    if cop.text == 'France':
        cop.click()
        break        # once the element is found then there is no need to look for other elements so 'break' it

# suppose instead of select tag there is div or button or some other tag.how to find option inside the dropdown
# we will write a Xpath for that and then we can store all the element and do whatever we want

opt_len = driver.find_elements(By.XPATH, "//*[@id='country']/option")
print('total number of option are :', len(opt_len))