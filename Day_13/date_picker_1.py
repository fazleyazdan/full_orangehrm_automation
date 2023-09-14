# there are two types of web elements
# 1: standard
# 2: non-standard also customized web elements

# standard web elements are same on every page or apps ie : button, image, checkboxes, radio button etc.
# non-standard elements are not same in every app they are custom designed by developers ie : date picker
# sometimes there is a dropdown and arrows, sometimes there is a table of dates in date picker. so it is custom designed
# 90 % of the time we will use 'send_keys' to input date in a date picker but some don't accept it and require proper logic
# that's why the script we write for a date picker may not work for a date picker in some other app.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.get('https://jqueryui.com/datepicker/')
driver.maximize_window()
# using send_keys method (in this methode first identify the datepicker format and then send keys in that format)

driver.switch_to.frame(0)  # as there is only 1 frame, so we have used index to access it. the dpicker inside the frame.
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys('08/17/1996')   # mm/dd/yyyy

# using logic to input date in a date picker.l
# in this type of method focus on the 'month' and 'year' and capture it.
# then  match it with the expected month and year that we want.
# click on the next arrow until the expected and captured year and month matches.
# will use while loop because we don't know the condition.

year = '2021'
month = 'August'
date = '17'

while True:
    driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  # click back arrow

# to click date first we have to capture all dates from table
# most of the time date are stored in a table that means rows and columns are used for

all_date = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for ele in all_date:
    if ele.text == date:
        ele.click()
        break
