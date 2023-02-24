from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r"/Users/vasiliykirnos/skillfactory/selenium_example/chromedriver")
driver.get("https://petfriends.skillfactory.ru/login")
sleep(2)
# assert "Python" in driver.title
login = driver.find_element(By.NAME, "email")
login.clear()
login.send_keys("123@a.ru")

sleep(2)

password = driver.find_element(By.NAME, "pass")
password.clear()
password.send_keys("123@a.ru")
sleep(3)
password.send_keys(Keys.RETURN)

sleep(10)
# assert "No results found." not in driver.page_source
driver.close()