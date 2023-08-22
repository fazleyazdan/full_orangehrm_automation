
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://testautomationpractice.blogspot.com/')

# handling checkboxes

# 1: handling single checkbox
# driver.find_element(By.XPATH, "//input[@id='sunday']").click()

# 2: handling multiple checkboxes
# to handle multiple check boxes we have to write an XPATH such that it captures all the checkboxes we want
# for this we have to look for common attribute. we want to click all the week days checkboxes
# now these checkboxes have one thing in common, and it is 'type' attribute which is 'checkbox'
# but it matches some extra element as well, so we have to look for something which makes them unique from other C.Boxes
# now there is other attribute 'id' it's unique, however in days name there is one thing common
# ie: 'sunday', 'monday' etc. now at the end of each word 'day' is common
# so, we will select all the other C.boxes using this strategy

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

# now to click multiple checkboxes we use for loop. there are two approaches for this
# approach 1: find the length of elements and traverse them.
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approach 2: straight forward. select all elements individually and then traverse.
# for checkbox in checkboxes:
#     checkbox.click()

# 3: select multiple checkboxes of your choice
# we have to get a unique attribute value for performing this task and write a condition based on that
# for checkbox in checkboxes:
#     week_names = checkbox.get_attribute('id')
#     if week_names == 'sunday' or week_names == 'saturday':
#         checkbox.click()

# 4: suppose we have many checkboxes, and we want to select the last 2 checkboxes
# we will use the range function in for loop and give it a starting index and total no of checkboxes
# for finding starting index (total no checkboxes - 2) :: 2 represents the last 2 checkboxes we want to select
# in range starting index starts from 0. length of checkboxes is 7 so the total indexes are 6.

# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

# 5: select first 2 checkboxes:
for i in range(len(checkboxes)):
    if i < 2:       # click the first 2 checkboxes. we have given condition that 'i' should be less than 2. ie 0,1 index
        checkboxes[i].click()

# 6: unselect all the checkboxes -- Methode 1: this methode well work if all the checkboxes are already selected
# for checkbox in checkboxes:
#     checkbox.click()

# Methode 2: we will give it a condition and then unselect only those checkboxes which are selected
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
