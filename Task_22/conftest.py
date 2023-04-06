import pytest
import requests
from settings import valid_email, valid_password
import json
from datetime import datetime


# @pytest.fixture(scope="class")  # , autouse=True
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")


@pytest.fixture(scope="class")  # , autouse=True
def auth_key():
    headers = {
        'email': valid_email,
        'password': valid_password
    }
    res = requests.get("https://petfriends.skillfactory.ru/" + 'api/key', headers=headers)
    status = res.status_code
    result = ""
    assert res.status_code == 200, 'Запрос выполнен неуспешно'
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    assert 'key' in result, 'В запросе не передан ключ авторизации'
    return result


@pytest.fixture(scope="class")
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')


@pytest.fixture()  # autouse=True
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


