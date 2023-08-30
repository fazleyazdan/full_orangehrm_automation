# sometimes on web data is in tabular form. also called HTML tables
# there are two types of tables         1: static table    2: dynamic table

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://testautomationpractice.blogspot.com/')

# 1: count no of rows and columns

rowsCount = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
# if you want to jump directly 'tr' and skip 'tbody' then just write '//'. eg "//table[@name='BookTable']//tr"

colCount = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))

print('no of rows: ', rowsCount, '-- no of columns: ', colCount)
print()
# 2: capture data from specific row and column

tb_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]")  # (row 5 col 1)
print(tb_data.text)
print()

# 3: read all the rows and columns data
# now for this we will use 2 loops (1 for iterating rows and another for columns)
# we will use range function in loop. we have to increment the total count as range function starts from 0.

# we will " parameterize the XPATH " by passing the 'r' and 'c'.for dynamic printing of rows and columns data
# there is special syntax for parameterizing the XPATH. convert r and c into string. write it in double quotes....
# and write '+' at the start and end of 'r' and 'c'

print("printing all rows and columns data...........")
for r in range(2, rowsCount+1):
    for c in range(1, colCount+1):  # when col data is retrieved for one row. the loop will go back to the outer loop and increment the row
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end="       ")   # we use end for printing the data in the same row. in quotation, we specify the space we need bw the two values
    print()  # for spacing bw the row values

print()
# 4: read data based on condition (print bookName if authorName equals to "ali")
# for this type of condition the col is constant because the author name is in col 2. and we only need to change the row dynamically

for r in range(2, rowsCount+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == 'Mukesh':
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text  # after finding the author name change col to 1 because the books name is in col 1
        print(bookName, "     ", authorName)

# you can also find subject names just by keeping the columns constant and keeping the rows dynamic

driver.close()