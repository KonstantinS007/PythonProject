import pytest
#
#
# def python_string_slicer(str):
#    if len(str) < 50 or "python" in str:
#        return str
#    else:
#        return str[0:50]
#
# def generate_id(val):
#    return "params: {0}".format(str(val))
#
#
# @pytest.fixture(scope="function", params=[
#    ("Короткая строка", "Короткая строка"),
#    ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#     , "Длинная строка, не то чтобы прям очень длинная, но"),
#    ("Короткая строка со словом python", "Короткая строка со словом python"),
#    ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#     , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
# ], ids=generate_id)
# def param_fun_generated(request):
#    return request.param
#
#
# def test_python_string_slicer_generated(param_fun_generated):
#    (input, expected_output) = param_fun_generated
#    result = python_string_slicer(input)
#    print("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
#    assert result == expected_output
#
# @pytest.fixture(scope="function", params=[
#    ("Короткая строка", "Короткая строка"),
#    ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#     , "Длинная строка, не то чтобы прям очень длинная, но"),
#    ("Короткая строка со словом python", "Короткая строка со словом python"),
#    ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#     , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python")
# ])
#
#
# def param_fun(request):
#    return request.param
#
#
# def test_python_string_slicer(param_fun):
#    (input, expected_output) = param_fun
#    result = python_string_slicer(input)
#    print ("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
#    assert result == expected_output


#
#
# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [10, 11])
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True
#
#
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True
#
#
# def ids_x(val):
#     return "x=({0})".format(str(val))
#
#
# def ids_y(val):
#     return "y=({0})".format(str(val))
#
#
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)
# @pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True


# @pytest.mark.parametrize(“r”, [0, 255])
# @pytest.mark.parametrize(“g”, [0, 15, 150, 255])
# @pytest.mark.parametrize(“b”, [0, 30, 255])
# def test_color_picker(r, g, b):
#     print(r, g, b)

# @pytest.fixture(autouse=True)
# def ket_api_key():
#    """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""
#
#    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#    status, pytest.key = pf.get_api_key(valid_email, valid_password)
#
#    # Сверяем полученные данные с нашими ожиданиями
#    assert status == 200
#    assert 'key' in pytest.key
#    yield
#    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
#    assert pytest.status == 200
#
#
# @pytest.mark.parametrize("filter", ['', 'my_pets'], ids= ['empty string', 'only my pets'])
# def test_get_all_pets_with_valid_key(filter):
#    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
#    Для этого сначала получаем api-ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
#    запрашиваем список всех питомцев и проверяем, что список не пустой.
#    Доступное значение параметра filter - 'my_pets' либо '' """
#
#    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)
#
#    assert len(result['pets']) > 0


@pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
@pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
def test_multiply_params(x, y):
   print("x: {0}, y: {1}".format(x, y))
   assert True


