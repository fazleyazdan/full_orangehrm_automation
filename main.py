from Tools.scripts.serve import app
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


os.environ['PATH'] += r"C:\Drivers\chromedriver_win32"
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(7)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

exp_title = driver.title
act_title = 'OrangeHRM'
if exp_title == act_title:
    print("test case passed!")
else:
    print("test case failed!")
# my_element = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")


