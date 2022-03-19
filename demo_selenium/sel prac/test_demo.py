from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from test_seleniumwrapper import Selenium_Wrapper
from test_config import Config

# Launches a new chrome browser
driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get(Config.URL)
sleep(3)

s = Selenium_Wrapper(driver)        # passing the driver instance that is created in 15th line
s.click_element((By.LINK_TEXT, "Register"))
s.click_element((By.ID, "gender-male"))
s.enter_text((By.NAME, "FirstName"), value="hello")
s.enter_text((By.NAME, "LastName"), value="world")
s.enter_text((By.ID, "Email"), value="njjmkhdjkhn@company.com")
s.enter_text((By.ID, "Password"), value="Password123")
s.enter_text((By.ID, "ConfirmPassword"), value="Password123")
s.click_element((By.ID, "register-button"))
# driver.close()