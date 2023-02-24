import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path='C:\\test\\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()

def test_show_my_pets():
    # Вводим email
    field_email = pytest.driver.find_element(By.ID, "email")
    field_email.send_keys(valid_email)

    # add password
    field_pass = pytest.driver.find_element(By.ID, "pass")
    field_pass.send_keys(valid_password + Keys.ENTER)

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "ЛЮБОВЬ ГУЛЬБИНА"

    #Проверка№1
    # количество строк в таблице
    #(проверка таблицы питомцев) явные ожидания элементов страницы.
    amount = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
    #количество Питомцев в профиле
    mypets = pytest.driver.find_element(By.XPATH, ('//body/div[1]/div[1]/div[1]'))
    num = mypets.get_attribute('innerText')
    #сравнение количества строк в таблице(минус заголовок) и числа в профиле
    assert str(len(amount) - 1) in num

    #Параметры питомцев оформляем в качестве переменных и записываем в список
    # Устанавливаем неявные ожидания(сек)
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(2)')
    # Устанавливаем неявные ожидания(сек)
    pytest.driver.implicitly_wait(10)
    types = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(3)')
    # Устанавливаем неявные ожидания(сек)
    pytest.driver.implicitly_wait(10)
    ages = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(4)')

    #Проверка №2  - У всех питомцев есть имя, возраст и порода.
    for i in range(len(ages)):
        assert ages[i].text != ''
        assert names[i].text != ''
        assert types[i].text != ''

    #Проверка №3 - хотя бы у половины питомцев есть фото
    # Устанавливаем неявные ожидания(сек)
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > th > img')
    number_image = 0
    half_num = float((len(amount) - 1)/2)

    for i in range(len(ages)):
        if images[i].get_attribute('src') != '':
            number_image += 1
        else:
            number_image = number_image
    assert number_image >= half_num

    #Проверка № 4- У всех питомцев разные имена
    setnames = set(names)
    assert len(names) == len(setnames)

    #Проверка № 5 - В списке нет повторяющихся питомцев.
    # Устанавливаем неявные ожидания(сек)
    pytest.driver.implicitly_wait(10)
    all_mypets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    unq_pets = []
    for pet in all_mypets:
        unq_pets.append(pet.text)
    assert len(set(unq_pets)) == len(unq_pets)

