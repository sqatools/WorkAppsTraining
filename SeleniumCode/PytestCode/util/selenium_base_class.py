class SeleniumBaseClass:
    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_data_field(self, data, locator):
        self.driver.find_element(*locator).send_keys(data)
