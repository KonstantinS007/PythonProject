import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
import time
#  pytest -v --driver Chrome --driver-path chromedriver.exe test_selenium.py


def test_show_my_pets(selenium):  # _driver
    ''' Тест на проверку списка питомцев:
       1. Проверяем, что оказались на странице питомцев пользователя.
       2. Проверяем, что присутствуют все питомцы.  '''
    
    driver = selenium
    driver.get("https://petfriends.skillfactory.ru/login")
    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    locator0 = ('css_selector', "a.nav-link[href='/my_pets']")
    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # 1. Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице
    locator1 = ('xpath', '//div[@class=".col-sm-4 left"]')
    pets_number = driver.find_element(*locator1).text.split('\n')[1].split(': ')[1]
    # pets_count = 100
    locator2 = ('xpath', '//table[@class="table table-hover"]/tbody/tr')
    pets_count = driver.find_elements(*locator2)
    assert int(pets_number) == len(pets_count)
    