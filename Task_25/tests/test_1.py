import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Task_25.settings import *
pytest.driver = webdriver.Chrome(executable_path='C:\\tests\\chromedriver.exe')
# Переходим на страницу авторизации
pytest.driver.get('https://petfriends.skillfactory.ru/login')

pet_email = pytest.driver.find_element(By.ID, 'email')
pet_email.send_keys(valid_email)
# Вводим пароль
field_pass = pytest.driver.find_element(By.ID, 'pass')
field_pass.send_keys(valid_password)
# Нажимаем на кнопку вход
pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
pytest.driver.implicitly_wait(10)
pytest.driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
name_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(2)')
setnames = set(names)
list_name_my_pets = []
for i in range(len(name_my_pets)):
    list_name_my_pets.append(name_my_pets[i].text)
set_pet_data = set(list_name_my_pets)  # преобразовываем список в множество
assert len(names) == len(setnames)
pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
pets = []
for pet in all_pets:
    pets.append(pet.text)
assert len(set(pets)) == len(pets)
pytest.driver.implicitly_wait(10)  # неявные ожидания
pets_number = pytest.driver.find_elements(By.XPATH, '//div[@class=".col-sm-4 left"]')
pets_number1 = pets_number[0].text.split('\n')[1].split(': ')[1]
pets_count = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
assert int(pets_number1) == len(pets_count)


with open('log.txt', 'a', encoding='utf8') as f:
    f.write(f'{name_my_pets}, \n {names}, \n{setnames}, \n{set_pet_data}, \n{pets}, \n{pets_number}, \n{pets_number1}')
pytest.driver.quit()
