# frame inside another frame is called inner frame.
# now to access elements inside the inner frame we have to switch to frame.
# there is no need to use default_content() because the inner frame is inside the outer frame which we have accessed.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('https://demo.automationtesting.in/Frames.html')

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
outerFrame = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outerFrame)   # passed frame as a web element

innerFrame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys('i found you!')

# if you want to switch back to the parent Iframe there is a special command for it.
driver.switch_to.parent_frame()
