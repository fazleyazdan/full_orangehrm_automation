# frames: when we want to embed something from the 3rd party into our website they are called Iframes.
# for example : if i want to embed google map into my website then I will use Iframes for that.
# when working with windows we call it frames and when working with web we call it Iframes
# tag name for frame:  'frame'  , 'Iframe'  , 'form': they all represents frame

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/WebDriver.html')

# webdriver cannot directly identify elements on Iframes. to tackle this issue we have to switch to Iframes first.
# inside the parenthesis we have to pass either name or id of the frame or, we can pass a frame as a web element
# if there is only 1 frame inside the web then good approach is to pass the index of the frame 0. ie: driver.switch_to.frame(0)
# webdriver cannot directly switch from one frame to another and it will give an exception...
# when you switch from main page to frame the driver is focused on that frame.now to switch to another frame...
# we have to go back to the main page and then from the main page switch to another frame.
# for that we will use driver.switch_to.default_content()

driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()
driver.switch_to.default_content()  # go back to the main page

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT, 'WebDriver').click()
driver.switch_to.default_content()


driver.switch_to.frame('classFrame')
driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/div[1]/ul/li[8]/a').click()