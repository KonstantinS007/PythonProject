import pytest
# import requests
# from config import email, password # __init__ see, no else all directory
# from datetime import datetime


# @pytest.fixture()
# def some_data():
#     return 42
#
#
# def test_some_data(some_data):
#     assert some_data == 42

# #  pytest -v -s -k "some_data"


# @pytest.fixture()
# def get_key():
#     # переменные email и password нужно заменить своими учетными данными
#     response = requests.post(url='https://petfriends.skillfactory.ru/login',
#                              data={"email": email, "pass": password})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     return response.request.headers.get('Cookie')
#
#
# def test_getAllPets(get_key):
#     response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
#                             headers={"Cookie": get_key})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

# # pytest -v -s -k "getAllPets"


# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")


# @pytest.fixture(scope="class", autouse=True) # 3
# def session_fixture():
#     print("\nclass fixture starts")
#
#
# @pytest.fixture(scope="function", autouse=True) # 2
# def function_fixture():
#     print("\nfunction fixture starts")


# @pytest.fixture(scope="session", autouse=True) # 1
# def function_fixture():
#     print("\nSession fixture starts")


# class TestClass23:
#
#     def test_first(self):
#         pass
#
#     def test_second(self):
#         pass


@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)