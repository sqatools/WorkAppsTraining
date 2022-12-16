from selenium import webdriver
from selenium.webdriver.common.by import By


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
driver.maximize_window()
# implicit wait : this applies on all the element on the web page on which we are working.
#driver.implicitly_wait(10)

# Explicit wait, fluent wait
wait = WebDriverWait(driver, 15, poll_frequency=2)

def get_element(locator, wait_condition=EC.element_to_be_clickable):
    try:
        elem = wait.until(wait_condition(locator))
        return elem
    except Exception as e:
        print("Element not found :", locator)
        print(e)

def click_element(locator):
    elem = get_element(locator)
    elem.click()

def send_text(locator, input):
    elem = get_element(locator)
    elem.send_keys(input)

male_locator = (By.ID, 'male123')
female_locator = (By.ID, 'female')
fromcity = (By.ID, 'fromcity')
destinationCity = (By.ID, 'destcity')
billing_name = (By.ID, 'billing_name')


click_element(male_locator)
click_element(female_locator)
send_text(fromcity, 'Mumbai')
send_text(destinationCity, 'Pune')
send_text(billing_name, 'SQA Tools')

time.sleep(5)
driver.close()





#get_element -> click_element()
#get_element -> send_text()





