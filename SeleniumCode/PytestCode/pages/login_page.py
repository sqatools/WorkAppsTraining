import sys
sys.path.append("E:\\Trainings\\PythonSeleniumWorkApp14Nov2022\\GitCode\\WorkAppsTraining\\SeleniumCode\\PytestCode")
from util.selenium_base_class import SeleniumBaseClass
from data.login_page_data import *


class LoginPage(SeleniumBaseClass):
    def __init__(self, driver):
        super().__init__(driver)


    def enter_fb_username(self, username):
        self.send_data_field(username, fb_username_field)

    def enter_fb_password(self, password):
        self.send_data_field(password, fb_password_field)

    def click_login_button(self):
        self.click_element(fb_login_button)
