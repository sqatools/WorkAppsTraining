from selenium import webdriver
from selenium.webdriver.common.by import By
"""
pip install webdriver-manager
"""
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as edgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from SeleniumCode.test_data import *

#driver = webdriver.Chrome(executable_path="E:\\Trainings\\PythonSeleniumWorkApp14Nov2022\\SeleniumCode\\driver\\chromedriver.exe")
#driver = webdriver.Chrome()
driver = None
if browser == 'chrome':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser == 'firefox':
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
elif browser == 'edge':
    driver = webdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))


driver.get(url)

driver.find_element(By.ID, 'email').send_keys('Selenium')

driver.find_element(By.ID, 'pass').send_keys('P@ssword')

driver.find_element(By.NAME, 'login').click()

driver.close()