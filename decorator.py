def edit_data(json):  # Укорачивает запись значений в лог
    try:
        list_of_pets = json["pets"]
    except KeyError:
        list_of_pets = [json]
    for i in list_of_pets:
        if len(i["pet_photo"]) > 10:
            i["pet_photo"] = i["pet_photo"][:10]
        if len(i["age"]) > 4:
            i['age'] = i['age'][:4]
        if len(i["animal_type"]) > 10:
            i['animal_type'] = i['animal_type'][:10]
        if len(i["name"]) > 10:
            i['name'] = i['name'][:10]
    return json


def post_api_log(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', encoding="UTF-8") as f:
            print("Request--------------------------------", file=f)
            print(f"Doing POST request to {args[0]}", file=f)
            try:
                print(f"Path parameters: {kwargs['params']}", file=f)
            except KeyError:
                print(f"No path parameters")
            print(f"Headers of request: {kwargs['headers']}", file=f)
            data_repr = repr(kwargs['data'])
            print(f"Request body: {data_repr}", file=f)
            value = func(*args, **kwargs)
            print("Response---------------------------------", file=f)
            response_code = repr(value)[10:-1]
            print(f"Code of answer to response - {response_code}", file=f)
            if value.status_code != 200:
                print(f"Response body: {value.text}")
            else:
                try:
                    print(f"Response body: {edit_data(value.json())}", file=f)
                except KeyError:
                    print(f"Response body: {value.json()}", file=f)
            print("  ")
            return value
    return wrapper


def get_api_log(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', encoding="UTF-8") as f:
            print("Request--------------------------", file=f)
            print(f"Doing GET request to {args[0]}", file=f)
            try:
                print(f"Parameters of path: {kwargs['params']}", file=f)
            except KeyError:
                print(f"Query parameter is not provided.", file=f)
            print(f"Headers of request: {kwargs['headers']}", file=f)
            value = func(*args, **kwargs)
            print("Response------------------------------", file=f)
            response_code = repr(value)
            print(f"Code of answer to response - {response_code}", file=f)
            if value.status_code != 200:
                print(f"Response body: {value.text}", file=f)
            else:
                try:
                    print(f"response body: {edit_data(value.json())}", file=f)
                except KeyError:
                    print(f"response body: {value.json()}", file=f)
            print("  ")
            return value

    return wrapper


def put_api_log(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', encoding="UTF-8") as f:
            print("Request---------------------------------", file=f)
            print(f"Doing PUT request to {args[0]}", file=f)
            print(f"Headers of request: {kwargs['headers']}", file=f)
            print(f"Parameters of request path pet_id: {kwargs['path']}", file=f)
            data_repr = repr(kwargs['data'])
            print(f"Request body: {data_repr}", file=f)
            value = func(*args, **kwargs)
            print(value)
            print("Response--------------------------------------", file=f)
            response_code = repr(value)
            print(f"Code of answer to response - {response_code}", file=f)
            if value.status_code != 200:
                print(f"Response body: {value.text}", file=f)
            else:
                try:
                    print(f"Response body: {edit_data(value.json())}", file=f)
                except KeyError:
                    print(f"Response body: {value.json()}", file=f)
            print("  ")
            return value
    return wrapper


def delete_api_log(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', encoding="Windows-1251") as f:
            print("Request-----------------------------------------")
            print(f"Doing DELETE response to {args[0]}", file=f)
            print(f"Headers of request: {kwargs['headers']}", file=f)
            print(f"Parameter of path request pet_id: {kwargs['path']}", file=f)
            value = func(*args, **kwargs)
            print("Response-------------------------------------------")
            response_code = repr(value)
            print(f"Code of answer to request- {response_code}", file=f)
            print("  ")
            return value
    return wrapper
