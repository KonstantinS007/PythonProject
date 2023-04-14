from selenium import webdriver as selenium_wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pytest


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.marketing_banner_locator = (By.XPATH, "//div[@class=\"btn btnOrange btnFlat js-popup-close\"]")
        self.destination_locator = (By.NAME, "destination")
        self.start_search_locator = (By.ID, "startSearch")

    def search_for_destination(self, destination_text):
        #  market_banner = self.driver.find_element(self.marketing_banner_locator)
        market_banner = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.marketing_banner_locator))
        market_banner.click()
        self.driver.implicitly_wait(10)
        destination_obj = self.driver.find_element(self.destination_locator)
        destination_obj.clear()
        destination_obj.send_keys(destination_text)
        sleep(2)
        start_search = self.driver.find_element(self.start_search_locator)
        start_search.click()

@pytest.fixture(scope="session")
def selenium_driver():
    s = Service(r"/Users/vasiliykirnos/skillfactory/qap_pytest/chromedriver")
    chrome_options = Options()
    driver = selenium_wd.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_search_for_destination(selenium_driver):
    selenium_driver.get("https://travelata.ru")
    home_page = HomePage(selenium_driver)
    home_page.search_for_destination("������")
    sleep(10)
