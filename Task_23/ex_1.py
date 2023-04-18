from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("http://www.python.org")
sleep(3)
assert "Python" in driver.title
locator = ('name', "q")
elem = driver.find_element(*locator)
sleep(3)
elem.clear()
sleep(3)
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

sleep(3)
assert "No results found." not in driver.page_source
driver.close()
