"""Модуль 19"""
import json
from requests_toolbelt.multipart import MultipartEncoder
import requests
from decorator import post_api_log, get_api_log, put_api_log, delete_api_log


@post_api_log
def post_request(url, headers, data):
    return requests.post(url=url, headers=headers, data=data)


@get_api_log
def get_request(url, headers, params=None):
    return requests.get(url=url, headers=headers, params=params)


@delete_api_log
def delete_request(url, headers, path):
    url = url + path
    return requests.delete(url=url, headers=headers)


@put_api_log
def put_request(url, headers, data, path):
    url = url + path
    return requests.put(url=url, headers=headers, data=data)


class PetFriends:
    """API библиотека к веб приложению Pet Friends"""

#    pytest test_pet_friends.py
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, passwd: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключом пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = ""):  # -> json
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком найденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = get_request(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str):
        """Метод отправляет (запрос) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        with open(pet_photo, 'rb') as f:
            foto = f.read()
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, foto, 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = post_request(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления об успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: str) -> json:
        """Метод отправляет запрос на сервер об обновлении данных питомца по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённый данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

# Новые модули запросов

    def add_new_pet_no_foto(self, auth_key: json, name: str, animal_type: str,
                            age: str) -> json:
        """Метод отправляет (запрос) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = post_request(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def update_pet_foto(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет запрос на сервер об обновлении фото по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённый данными питомца"""
        with open(pet_photo, 'rb') as f:
            foto = f.read()

        data = MultipartEncoder({
                'pet_photo': (pet_photo, foto, 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = post_request(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_foto_png(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет запрос на сервер об обновлении фото по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённый данными питомца"""
        with open(pet_photo, 'rb') as f:
            foto = f.read()

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/png')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = post_request(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets_cooki(self, auth_key, filter: str = "") -> json:

        headers = {'Cookie': auth_key}
        filter = {'filter': filter}

        res = get_request(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def get_api_key1(self, email: str, passwd: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключом пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets1(self, auth_key: json, filter: str = ""):  # -> json
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком найденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet_simple1(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result