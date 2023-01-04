from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as edgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from GitCode.WorkAppsTraining.SeleniumCode.test_data import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = None
if browser == 'chrome':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser == 'firefox':
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
elif browser == 'edge':
    driver = webdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
driver.maximize_window()
# implicit wait : this applies on all the element on the web page on which we are working.
#driver.implicitly_wait(10)

# Explicit wait, fluent wait
wait = WebDriverWait(driver, 15, poll_frequency=2)
alert = Alert(driver)

"""
driver.find_element(By.ID, 'btnShowMsg').click()
time.sleep(2)
print(alert.text)
alert.accept()
"""
time.sleep(2)

# Second pop alert
"""
driver.find_element(By.ID, 'button').click()
time.sleep(2)
print(alert.text)
#alert.accept()
alert.dismiss()
time.sleep(2)
get_msg = driver.find_element(By.ID, 'demo').text
print(get_msg)
assert get_msg == 'You pressed OK!'
"""

# Third alert provide input

driver.find_element(By.ID, 'promptbtn').click()
time.sleep(3)
alert.send_keys("SQA Tools")
alert.accept()

get_msg = driver.find_element(By.ID, 'prompt').text
print(get_msg)
time.sleep(3)

assert get_msg == 'Hello SQA Tools! How are you today?'
driver.close()




