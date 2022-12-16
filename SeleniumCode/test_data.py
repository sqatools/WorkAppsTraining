from selenium.webdriver.common.by import By
browser = 'chrome'
url = 'https://www.facebook.com/'

link_locator = (By.XPATH, "//a[contains(@href,'')]")