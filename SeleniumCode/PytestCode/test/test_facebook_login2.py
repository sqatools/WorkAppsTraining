import pytest
import unittest
from selenium.webdriver.common.by import By
import time
import sys

sys.path.append("E:\\Trainings\\PythonSeleniumWorkApp14Nov2022\\GitCode\\WorkAppsTraining\\SeleniumCode\\PytestCode")
from data.login_page_data import *
from pages.login_page import LoginPage

@pytest.mark.usefixtures("initial_config", "get_config")
class TestFacebookSearch(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)

    #@pytest.mark.usefixtures("get_config")
    def test_login_facebook(self):
        self.lp.enter_fb_username("admin")
        self.lp.enter_fb_password("P@ssword")
        self.lp.click_login_button()
        time.sleep(5)

    #@pytest.mark.usefixtures("get_config")
    def test_login_facebook2(self):
        self.lp.enter_fb_username("admin2")
        self.lp.enter_fb_password("P@ssw0rd2")
        self.lp.click_login_button()
        time.sleep(5)






