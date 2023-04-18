from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.tutu.ru/")
sleep(5)
locator = ('css selector', "#wrapper > div.l-screen-top.j-top-screen.s-tab-avia > div.l-search_forms > div > div.j-search_form.j-avia_search_form.search_form.tab_active > div > div.inputs_line.j-row.j-main.j-last_row > div.input_wrp.j-city_container.j-city_container_from > div.b-input__form__standart.m-avia_form.j-input_wrapper > input")
origin = driver.find_element(*locator) # By.CSS_SELECTOR, "#wrapper > div.l-screen-top.j-top-screen.s-tab-avia > div.l-search_forms > div > div.j-search_form.j-avia_search_form.search_form.tab_active > div > div.inputs_line.j-row.j-main.j-last_row > div.input_wrp.j-city_container.j-city_container_from > div.b-input__form__standart.m-avia_form.j-input_wrapper > input"
origin.clear()
origin.send_keys("Москва")
locator1 = ('xpath', "//*[text()='Москва (Россия)']")
WebDriverWait(driver, timeout=10).until(
    EC.visibility_of_element_located(locator1) #  (By.XPATH, "//*[text()='Москва (Россия)']")
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


date_to = driver.find_element(By.CSS_SELECTOR, "*[name=\"date_back\"]")
date_to.click()
date_to.send_keys("23.02.2023")
date_from.send_keys(Keys.RETURN)

sleep(10)
# assert "No results found." not in driver.page_source
driver.close()
#
# python -m pytest -v ex_3.py