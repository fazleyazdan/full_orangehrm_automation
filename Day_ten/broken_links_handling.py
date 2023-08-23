import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get('http://www.deadlinkcity.com/')

# for handling broken links we need to install 'requests' package/module.
# broken links does not have any target page
# we need to identify which one is broken link and which one is normal
# broken links response is always equal to or greater than 400

# first capture all links
all_links = driver.find_elements(By.TAG_NAME, 'a')
count = 0  # counter for broken links
count1 = 0  # counter for normal links
for link in all_links:
    url = link.get_attribute('href')  # get all the URL of the links
    try:    # during the request-response process network error may occur. good practice to use try-catch
        response = requests.head(url)  # hit the server with the url and store the response
    except:
        None   # means ignore all exception

# one of the things which comes with response is the status code.
    if response.status_code >= 400:
        print(url, 'broken url')
        count += 1
    else:
        print(url, 'valid link')
        count1 += 1

print('total no of broken links: ', count)
print('total no of normal links: ', count1)