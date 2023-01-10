import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.append("E:\\Trainings\\PythonSeleniumWorkApp14Nov2022\\GitCode\\WorkAppsTraining\\SeleniumCode\\PytestCode")

# E:\Trainings\PythonSeleniumWorkApp14Nov2022\GitCode\WorkAppsTraining\SeleniumCode\PytestCode
from data.constants import *
from util.selenium_base_class import SeleniumBaseClass
import os
import json

@pytest.fixture(scope='session')
def get_config():
    file_path = os.path.join(os.getcwd(), 'configuration.json')
    file = open(file_path)
    config_data = json.load(file)
    return config_data

@pytest.fixture(scope="class")
def initial_config(request, get_config):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(get_config['url'])
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()



@pytest.fixture(scope='function')
def smoke_setup():
    print("\n Smoke Initial Setup  done")
    yield
    print("\n Smoke setup cleanup  done")

@pytest.fixture(scope='session')
def regression_setup():
    print("\n Regression Initial Setup  done")
    yield
    print("\n Regression cleanup  done")

@pytest.fixture(scope='class')
def class_setup():
    print("\b class setup done")
    yield
    print("\n class setup cleanup done")


@pytest.fixture
def notscop_setup():
    print("\b no scope setup done")
    yield
    print("\n no scope setup cleanup done")

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #driver.get("https://")
    request.cls.workapp = SeleniumBaseClass(driver)
    yield
    driver.close()

@pytest.fixture(scope='class')
def get_url(request):
    request.cls.url = web_url
