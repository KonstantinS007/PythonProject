import requests
import pytest
import functools


def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"{args[1]} {args[2]}\n")
            f.write(f"Request headers: {args[0].headers}\n")
            response = func(*args, **kwargs)
            f.write(f"Request body: {response.request.body}\n")
            f.write(f"Response status code: {response.status_code}\n")
            f.write(f"Response headers: {response.headers}\n")
            f.write(f"Response body: {response.text}\n\n")
        return response

    return wrapper


@log_request
def api_request(session, method, url,
                headers_update='', data='', json=''):
    if headers_update is not None:
        session.headers.update(headers_update)
    if method == "GET":
        response = session.get(url, data=data, json=json)
    elif method == "POST":
        response = session.post(url, data=data, json=json)
    elif method == "DELETE":
        response = session.delete(url, data=data, json=json)
    elif method == "PUT":
        response = session.put(url, data=data, json=json)
    else:
        response = ''

    return response


BASE_URL = "https://petfriends.skillfactory.ru/api"

user = "123@a.ru"
password = "123@a.ru"


@pytest.fixture(scope="module")
def api_client():
    session = requests.Session()
    response = api_request(session, "GET", f"{BASE_URL}/key",
                           headers_update={
                               "email": user,
                               "password": password})
    access_token = response.json().get("key")
    assert access_token is not None

    session.headers.update({
        "auth_key": access_token,
        "accept": "application/json"})

    yield session

    api_request(session, "GET", f"{BASE_URL}/logout")


@pytest.fixture(scope="function")
def create_pet(api_client):
    data = {
        "name": "Fluffy",
        "age": 5,
        "animal_type": "cat"
    }
    response = api_request(api_client, "POST", f"{BASE_URL}/create_pet_simple", json=data)
    pet_id = response.json()["id"]

    yield pet_id

    api_request(api_client, "DELETE", f"{BASE_URL}/pets/{pet_id}")


def test_get_pets(api_client):
    response = api_request(api_client, "GET", f"{BASE_URL}/pets")
    assert response.status_code == 200
    assert len(response.json().get("pets")) > 0


def test_create_pet(create_pet):
    assert create_pet is not None


def test_update_pet(create_pet, api_client):
    data = {
        "name": "Maximus"
    }
    response = api_request(api_client, "PUT", f"{BASE_URL}/pets/{create_pet}", json=data)
    assert response.status_code == 200
    assert response.json().get("name") == "Maximus"