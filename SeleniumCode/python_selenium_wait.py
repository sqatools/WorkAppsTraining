from selenium import webdriver
from selenium.webdriver.common.by import By
"""
pip install webdriver-manager

Implicit wait
Explicit Wait, 
Fluent Wait
Static Wait
"""


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as edgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from SeleniumCode.test_data import *
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None
if browser == 'chrome':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser == 'firefox':
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
elif browser == 'edge':
    driver = webdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# implicit wait : this applies on all the element on the web page on which we are working.
driver.implicitly_wait(10)


# Explicit wait, fluent wait
wait = WebDriverWait(driver, 15, poll_frequency=2)


"""
t1 = time.time()
try:
    driver.find_element(By.ID, 'fromcity223').send_keys("Mumbai")
except:
    pass
t2 = time.time()

print("time taken:", t2 - t1)
"""

"""
try:
    t1 = time.time()
    elem = wait.until(EC.element_to_be_clickable((By.ID, 'destcity2345')))
    elem.send_keys('Pune')
except:
    pass
"""

t1 = time.time()
try:
    elem = driver.find_element(By.ID, "billing_name22")
except:
    pass
time.sleep(20)  # static wait
elem.send_keys("SQA Tools")
t2 = time.time()

print("element2 total time:", t2 - t1)

driver.close()




