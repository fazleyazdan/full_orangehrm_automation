# whenever you are requesting data from the server, the response may be delayed
# so in that case synchronization problem may arise
# now in a scenario like that it is a good practice to use wait commands specially implicit wait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# this will prevent the browser from automatically closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

# pros:
# now implicit wait have to be used once in a script, and it is available for the entire code until the driver is alive
# meaning it works for all the statement which comes after it.
# where ever the synchronization problem may occur it will handle it
# driver is only killed when you 'close' or 'quit' the driver. ie 'driver.quit'

# if a response takes 5 sec to display an element. and we specified 10 sec to wait
# in that case imp wait will use the 5 sec and as soon as the element is displayed it won't wait
# and will jump to next statement resulting in speedy script and good performance

# cons:
# if the element is not available within the mentioned time there is chance of getting exception
driver.implicitly_wait(10)  # max time wait standard is 10 sec

driver.get('https://www.google.com/')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')

# if you want to click enter button from your keyboard we use 'submit'
search_box.submit()

# we have searched for selenium and the server will show us the result
# now there is a chance to get synchronization problem because the response from the server may be delayed

# time.sleep(5)
# now in this case we can use time.sleep(). it is not in selenium and is native to python only
# you have to import it

# cons:
# 1: if the element is available within 2 seconds of the mentioned time, and
# we have given 5 seconds then 3 seconds will be wasted due to which script time is increased
# 2: if the element is not available within the mentioned time then there is chance of getting Exception
# 3: you have to write it every time you think the synchronization problem may occur


# Pros:
# 1: simple to use
# 2: Sometimes, a javascript function that change the inner text of the element which takes sometime.
# In that case only hard wait can be used because the element is already present,
# 'implicit wait and explicit wait will get the element before the inner text of the element
# changes resulting in no errors but wrong results.

# identify the link on the web which have text 'Selenium' and click. we created rel XPATH for that
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

# if you want to catch exception or handle the exceptions automatically we use try catch block in imp.wait


