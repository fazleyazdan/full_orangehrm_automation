from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# this will prevent the browser from automatically closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

# explicit wait works based on the condition and not on the time
# explicit wait have 2 parts one is declaration and the other is utilization/usage
# it takes 2 arguments in declaration 'driver' & time (in seconds)
# we use webdriver for explicit wait

# here I have used webDriverWait class and made an object of that class ie 'myWait'
# we wil use the object further
# myWait = WebDriverWait(driver, 10)  # basic explicit wait declaration syntax

# advanced declaration syntax
myWait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException])
# or instead of writing all those exceptions we can just write 'Exception' and it will handle all exceptions
# as the  maximum time out is 10 secs. we use poll frequency to look for the element  after every 2 secs
# if the element is located in the first cycle of p.frequency then the script will move on to next statements
# if element is not found.then poll.frequency will look for the element 5 times in those 10 sec until it is located
# poll frequency should always be less than maximum time out ie 'p.frequency < 10'

driver.get('https://www.google.com/')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')

# if you want to click enter button from your keyboard we use 'submit'
search_box.submit()

# now if there is chance of synchronization problem
# there is no need to use find_element because in explicit wait it is inclusive
# there is a class called 'EC' (expected condition) we will use this with the object. you have to import 'EC'
# here we are using the condition with EC. until that condition is satisfied/true the script will wait

# cons:
# 1: if the condition is not satisfied then after time that we have specified in declaration ....
# will throw an exception , or we can handle the exception automatically by specifying them in declaration
# 2: explicit wait is not a single statement you have to insert it multiple times

# pros:
# more effective because there is exception handling mechanism as well

searchLink = myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchLink.click()

driver.quit()