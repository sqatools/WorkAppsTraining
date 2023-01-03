from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as edgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from SeleniumCode.generic_selenium_previous import *
from SeleniumCode.test_data import *
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
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.maximize_window()
# implicit wait : this applies on all the element on the web page on which we are working.
#driver.implicitly_wait(10)

# Explicit wait, fluent wait
wait = WebDriverWait(driver, 15, poll_frequency=2)

elem = driver.find_element(By.XPATH, "//a[contains(text(), ' What is Manual Testing ')]")
elem.click()

windows = driver.window_handles
print(windows)
time.sleep(5)
driver.switch_to.window(windows[1])

heading  = driver.find_element(By.XPATH, "//h3[contains(text(), 'Manual Testing')]")
assert heading

driver.find_element(By.XPATH, "//a[contains(text(), 'Python 3 Tutorial')]").click()

time.sleep(5)

driver.switch_to.window(windows[0])
driver.find_element(By.XPATH, "//a[contains(text(), 'Home')]").click()

time.sleep(5)

driver.close()




