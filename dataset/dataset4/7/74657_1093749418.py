from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps, executable_path="C:\\Utility\\BrowserDrivers\\geckodriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(20)