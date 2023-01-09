import pytest
from selenium.webdriver.common.by import By
import time
import sys
sys.path.append("E:\\Trainings\\PythonSeleniumWorkApp14Nov2022\\GitCode\\WorkAppsTraining\\SeleniumCode\\PytestCode")
from util.selenium_base_class import SeleniumBaseClass
from data.login_page_data import *
driver = None
@pytest.mark.usefixtures("get_driver", "get_url")
class TestFacebookSearch():

    def test_launch_browser(self):
        self.workapp.launch_browser(self.url)

    def test_username(self):
       self.workapp.send_keys('user1@gamil.com', fb_username_field)
       time.sleep(5)

    def test_password(self):
       self.workapp.send_keys('P@ssword', fb_password_field)
       time.sleep(5)

    def click_to_login(self):
        self.workapp.element_click(fb_login_button)
        time.sleep(5)




