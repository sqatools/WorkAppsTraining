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
