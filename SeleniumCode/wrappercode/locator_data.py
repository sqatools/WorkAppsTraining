from selenium.webdriver.common.by import By

male_locator = (By.ID, 'male')
female_locator = (By.ID, 'female')
fromcity = (By.ID, 'fromcity')
destinationCity = (By.ID, 'destcity')
billing_name = (By.ID, 'billing_name')
billing_phone = (By.ID, 'billing_phone')
billing_email = (By.ID, 'billing_email')

first_name_loc = (By.XPATH, "(//input[@id='firstname'])[1]")
last_name_loc = (By.XPATH, "(//input[@id='firstname'])[2]")