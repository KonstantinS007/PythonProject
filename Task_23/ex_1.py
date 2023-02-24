from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r"/Users/vasiliykirnos/skillfactory/selenium_example/chromedriver")
driver.get("http://www.python.org")
sleep(10)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
sleep(10)
elem.clear()
sleep(10)
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

sleep(10)
assert "No results found." not in driver.page_source
driver.close()
