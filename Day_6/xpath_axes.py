from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Environment Setup
os.environ['PATH'] += r"C:\Drivers\chromedriver_win32"
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager(version="114.0.5735.90").install()))

# visiting website
driver.maximize_window()
driver.get("https://money.rediff.com/index.html")

# used implicit wait so that the website can properly load and then the driver perform other actions
driver.implicitly_wait(4)

# self: Selects the current node itself.
# child: Selects all child elements of the current node.
# descendant: Selects all descendants (children, grandchildren, etc.) of the current node.
# parent: Selects the parent of the current node.
# ancestor: Selects all ancestors (parent, grandparent, etc.) of the current node.
# following-sibling: Selects all siblings that come after the current node.
# preceding-sibling: Selects all siblings that come before the current node.
# following: Selects all nodes that come after the current node in the document order.
# preceding: Selects all nodes that come before the current node in the document order.
# for better understanding watch SDET selenium with python lecture 4

# extracting the text of 'a' tag using XPATH axes 'self'
# I have made this element a self element. now i can navigate from this element to  other element

# Due to the constant changes in web the element text can change and the compiler can throw an error
# therefore you are advised to check the element because you may be seeing this code years after its creation
self_txt = driver.find_element(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/self::a")
print(self_txt.text)

# parent

parent_txt = driver.find_element(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/parent::*")
print(parent_txt.tag_name)

# child
# as the element which i have made 'self' does not have any child element that's why I first located the parent of self
# and then located the child of that parent which is the 'self' element itself i.e 'a' and  printed it
# just to check the 'child' axes is working fine

# parent_txt = driver.find_element(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/parent::*/child::")
# child_txt = driver.find_element(By.XPATH, "//a[contains(text(),'Gland Pharma')]/parent::h4/child::a")
# print(child_txt.tag_name)

# ancestor
ancestor_txt = driver.find_element(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/ancestor::ul")
print(ancestor_txt.text)

# descendant
# if you don't know how many descendant elements are here just put '*'
# if you are targeting multiple element then use 'find_elements' instead of element

descendant_txt = driver.find_elements(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/ancestor::ul/descendant::*")
print('number of descendant nodes are:', len(descendant_txt))

# following
following_txt = driver.find_elements(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/ancestor::ul/following::*")
print('number of following nodes are:', len(following_txt))

# preceding
preceding_txt = driver.find_elements(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/ancestor::ul/preceding::*")
print('number of preceding nodes are:', len(preceding_txt))

# following-sibling
following_s_txt = driver.find_elements(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/ancestor::ul/following-sibling::*")
print('number of following-sibling nodes are:', len(following_s_txt))

# preceding-sibling
preceding_s_txt = driver.find_elements(By.XPATH, "//a[contains(text(),'S&P BSE 200')]/ancestor::ul/preceding-sibling::*")
print('number of preceding-sibling nodes are:', len(preceding_s_txt))


driver.close()
