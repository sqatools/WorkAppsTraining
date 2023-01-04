from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
import time
import datetime
import os

"""
screenshot
java script
Action
"""

driver.get("https://www.google.co.in")
driver.maximize_window()
driver.implicitly_wait(10)
cur_path = os.getcwd()
log_path = os.path.join(cur_path, 'log')
if not os.path.isdir(log_path):
    os.mkdir(log_path)


def search_data_on_google():
    try:
        driver.find_element(By.NAME, 'q').send_keys("Python")
        driver.find_element(By.NAME, 'btnK').click()
        assert driver.find_element(By.XPATH, "//h3[text()='Welcome ']")
    except Exception as e:
        cur_date = datetime.datetime.now().strftime("%Y_%m_%d_%h_%m")
        screenshot_path = os.path.join(log_path, f'python_search_{cur_date}.png')
        print(screenshot_path)
        #driver.save_screenshot(f'python_search_{cur_date}.png')
        driver.save_screenshot(screenshot_path)
        raise e

#search_data_on_google()
def execute_java_script():
    driver.get('https://www.facebook.com/')
    time.sleep(5)
    output = driver.execute_script("return document.title")
    print(output)
    output2 = driver.execute_script("return document.URL")
    print(output2)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)


execute_java_script()

driver.close()

