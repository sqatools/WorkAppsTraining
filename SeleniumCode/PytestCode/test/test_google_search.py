import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("get_driver", "get_url")
class TestGoogleSearch:

    def test_launch_browser(self):
        self.workapp.launch_browser(self.get_url)

    def test_input(self):
        self.workapp.find_element(By.NAME, "q").send_keys("Python")

    def test_click_button(self):
        self.workapp.find_element(By.NAME, "btnK").click()

    # def test_open_facebook(self):
    #     self.workapp.get(self.url)
    #     time.sleep(5)

