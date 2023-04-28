from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
# pytest test_pet.py
@pytest.fixture(autouse=True)
def testing():

   #pytest.driver = webdriver.Chrome('//chromedriver.exe')
   pytest.driver = webdriver.Chrome(executable_path='//chromedriver.exe')
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   pytest.driver.set_window_size(1920, 1080)
   yield

   pytest.driver.quit()


def test_show_my_pets():
   #  email
   pytest.driver.find_element(By.ID, 'email').send_keys('uzerovalex9@gmail.com')
   #
   pytest.driver.find_element(By.ID, 'pass').send_keys('qwerty123')
   time.sleep(3)
   #
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   #
   time.sleep(3)
   # assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   pytest.driver.find_element(By.CLASS_NAME, 'nav-link').click()

   time.sleep(3)

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   print(range(len(names)))
   print(f'{names}')
   print(f'{len(names)=}')
   for i in range(len(names)):
      assert images[i].get_attribute('scr') != ''
      # assert names[i].text != ''
      assert descriptions[i].text != ''
      # assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
