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
import time

driver = None
if browser == 'chrome':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser == 'firefox':
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
elif browser == 'edge':
    driver = webdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))

#url = 'https://automationbysqatools.blogspot.com/2021/05/dummy-website.html'
url = "https://automationbysqatools.blogspot.com/p/home.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
element_list = driver.find_elements(By.XPATH, "//div[@align='left']//ul//child::li/input")
print(element_list, len(element_list))

"""
for elem in element_list:
    elem.click()
    time.sleep(2)


# Select checkboxes with city name
city_list = ['Mumbai', 'Pune', 'Indore', 'Kolkata', 'Hyderabad', 'Orangabad', 'Delhi']
for city in city_list:
    check_box_xpath = f"//td[text()='{city}']//parent::tr//input"
    elem = driver.find_element(By.XPATH, check_box_xpath)
    elem.click()
    time.sleep(1)
    
"""
"""
country_name = 'Belarus'
driver.find_element(By.ID, 'billing_country').click()
driver.find_element(By.XPATH, f"//*[contains(text(), '{country_name}')]").click()
time.sleep(5)
driver.close()
"""

##### get_all_link  ####

link_elements = driver.find_elements(*link_locator)
for link in link_elements:
    link_text = link.text
    attr_val = link.get_attribute('href')
    print(link_text)
    print(attr_val)
    print("_"*60)

