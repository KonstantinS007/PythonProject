import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Task_25.settings import *
# pytest test_selen.py


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path='C:\\tests\\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()

def test_show_my_pets():
    # Вводим email
    pet_email = pytest.driver.find_element(By.ID, 'email')
    pet_email.send_keys(valid_email)
    # Вводим пароль
    field_pass = pytest.driver.find_element(By.ID, 'pass')
    field_pass.send_keys(valid_password)
    # Нажимаем на кнопку вход
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем с явным ожиданием, что мы авторизовались и оказались на главной странице /all_pets
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "// button[contains(text(), 'Выйти')]")))
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


    # Переходим на страницу питомцев пользователя
    pytest.driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    # Проверяем что логин соответствует авторизации
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == user
    # Проверяем наличие элементов
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr')))
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > th > img')))
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]')))

    # Проверка 1
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице
    pytest.driver.implicitly_wait(10)
    pets_number = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # Явные ожидания загрузки блока таблицы питомцев
    pets_count = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    assert int(pets_number) == len(pets_count)

    # Проверка 2 - У всех питомцев есть имя, возраст и порода

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(2)')

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    types = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(3)')

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    ages = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(4)')

    for i in range(len(ages)):
        assert ages[i].text != ''
        assert names[i].text != ''
        assert types[i].text != ''

    # Проверка 3 - хотя бы у половины питомцев есть фото

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > th > img')
    number_image = 0
    half_num = float((len(pets_count) - 1)/2)

    for i in range(len(ages)):
        if images[i].get_attribute('src') != '':
            number_image += 1
        else:
            number_image = number_image
    assert number_image >= half_num

    # Проверка 4 - У всех питомцев разные имена

    # pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    # names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(2)')
    # list_names = []
    # for i in range(len(names)):
    #     list_names.append(names[i].text)
    # setnames = set(list_names)
    #
    # assert len(names) == len(setnames)

    # Проверка 5 - В списке нет повторяющихся питомцев.

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pets = []
    for pet in all_pets:
        pets.append(pet.text)
    assert len(set(pets)) == len(pets)



