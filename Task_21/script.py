# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
# parent()


# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
#
# # Скопировать и вставить в консоль пайтон либо через принт
# print(parent(1))
# first = parent(1)
# second = parent(2)
# print(first())
# print(second())

# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# def my_first_decorator():
#     print("Это мой первый декоратор!")
#
#
# my_first_decorator = my_decorator(my_first_decorator)
# my_first_decorator()
#
#
# from decorators import do_twice
#
# @do_twice
# def test_twice():
#     print("Это вызов функции test_twice!")
#
# test_twice()

# from decorators import do_twice
# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# test_twice("Попытаемся вызвать функцию с аргументом")


# @do_twice
# def test_twice_without_params():
#     print("Этот вызов без параметров")
#
#
# @do_twice
# def test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# test_twice_without_params()
# test_twice_2_params("1", "2")
# test_twice("single")


# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
# decorated_value = test_twice("single")
# print(decorated_value)
# from decorators import do_twice
# import inspect

# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
#
# print(test_twice.__name__)

# @debug
# def age_passed(name, age=None):
#   if age is None:
#     return "Необходимо передать значение age"
#   else:
#     return "Аргументы по умолчанию заданы!"
#
# age_passed("Роман")
# age_passed("Роман", age=21)
# from decorators impodo_twicert
#
# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
# decorated_value = test_twice("single")
# print(age_passed.__init__)
# from decorators import debug
#
#
# @debug
# def age_passed(name):
#   if age is None:
#     return "Необходимо передать значение age"
#   else:
#     return "Аргументы по умолчанию заданы!"
#
#
# age_passed("Роман")


def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"


print(test_twice.__name__)
