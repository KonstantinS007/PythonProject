from xml.dom.minidom import Element
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.r
from time import sleep

driver = webdriver.Chrome(executable_path=r"/Users/vasiliykirnos/skillfactory/selenium_example/chromedriver")
driver.get("https://www.tutu.ru/")
sleep(5)

origin = driver.find_element(By.CSS_SELECTOR, "*[name=\"city_from\"]")
origin.clear()
origin.send_keys("Москва")

WebDriverWait(driver, timeout=10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[text()='Москва (Россия)']"))
)

origin_choice = driver.find_element(By.XPATH, "//*[text()='Москва (Россия)']")
origin_choice.click()

destination = driver.find_element(By.CSS_SELECTOR, "*[name=\"city_to\"]")
destination.clear()
destination.send_keys("Владивосток")


wait = WebDriverWait(driver, 
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]
            )
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[text()='Владивосток (Россия)']"))
)

destination_choice = driver.find_element(By.XPATH, "//*[text()='Владивосток (Россия)']")
destination_choice.click()

sleep(2)

date_from = driver.find_element(By.CSS_SELECTOR, "*[name=\"date_from\"]")
date_from.click()
date_from.send_keys("09.02.2023")
date_from.send_keys(Keys.RETURN)


date_to = driver.find_element(By.CSS_SELECTOR, "*[name=\"date_to\"]")
date_to.send_keys("23.02.2023")
date_from.send_keys(Keys.RETURN)

sleep(10)
# assert "No results found." not in driver.page_source
driver.close()
