# print("asdfg")
# a = 3.14
# b = '3.14'
#
# print(type(a))
# # <class 'float'>
# print(type(b))
# # <class 'str'>
# age = 25
#
# my_age = "I'm " + str(age)
# print(my_age)
# # здесь возникнет ошибка
# # TypeError: must be str, not in
# wow = 'wow'
#
# print(wow*5) # никакой ошибки не возникает
# # wowwowwowwowwow
# age = 25
#
# my_age = "I'm %x years old" % (age) # в шаблоне присутствует специальный символ %d
# d%
# print(my_age)
# # I'm 25 years old
# pi = 31.4159265
# print ("%.4e" % (pi))
# day = 14
# month = 2
# year = 2012
#
# print("%d.%02d.%d" % (day, month, year))
# # 14.02.2012
# print("%d-%02d-%d" % (year, month, day))
# # 2012-02-14
# print("%d/%d/%d" % (year, day, month))
# # 2012/14/2
# имеем список с числами с плавающей точкой
# L = [3.3, 4.4, 5.5, 6.6]
#
# # печатаем сам объект map
# print(map(round, L)) # к каждому элементу применяем функцию округления
# # <map object at 0x7fd7e86eb6a0>
#
# # и результат его преобразования в список
# print(list(map(round, L)))
# # [3, 4, 6, 7]
# L = ['3.3', '4.4', '5.5', '6.6']
#
# print (list (map ( float, L)))
# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# print(list_of_strings) # вывод списка чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
# list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]
# print(list_of_numbers)
# list_sum = sum(list_of_numbers)
# list_of_numbers.append(list_sum)
# print(list_of_numbers)
# 1 1 2 3 5 8 13 21 34 55
# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(int, input().split()))
#
# # обмениваем первое и последнее число
# # с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]
#
# # находим сумму и добавляем её в конец списка
# L.append(sum(L))
#
# print(L)
# person = {} # с помощью фигурных скобок можно создать словарь
#
# # словарь заполняется по принципу - ключ:объект (через двоеточие)
# person = {'Name' : 'Ivan Petrov'}
#
# # в него можно также добавлять новые объекты по ключу
# person['Age'] = 25
# person['Email'] = 'ivan_petrov@example.com'
# person['Phone'] = '8(800)555-35-35'
#
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# print(person.keys())
# # dict_keys(['name', 'age', 'email', 'phone'])
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys)))
# book = {}
# book['title'] = input('title: ')
# book['author'] = input('author: ')
# book['year'] = int(input('year: '))
# print(book)
# title = input("Введите название книги:")
# author = input("Введите фамилию автора:")
# year = int(input("Введите год издания:"))
#
# book = {'title': title,
#         'author': author,
#         'year': year}
#
# print(book)
# book = {}
# book['title'] = "Замученый студент" #input('title: ')
# book['author'] = "Автор модуля" #input('author: ')
# book['year'] = 1 #int(input('year: '))
# print(book)
# book = {}
# book['title'] = 'Алиса в стране чудес' #input('title: ') 'Алиса в стране чудес'
# book['author'] = 'Кэрролл' #input('author: ') 'Кэрролл'
# book['year'] = 1865 #int(input('year: ')) '1865'
# print(book)
# Допишите в задании вводные данные
# Допишите в задании вводные данные
# title = 'Алиса в стране чудес' #input("Введите название книги:") #'Алиса в стране чудес'
# author = 'Кэрролл' #input("Введите фамилию автора:") #'Кэрролл'
# year = '1865' #int(input("Введите год издания:")) #'1865'
# book = {'title' : title,
#         'author' : author,
#         'year' : int(year)}
#book = {}
#book['title'] = title #'Алиса в стране чудес' #input('title: ') --'Алиса в стране чудес'
#book['author'] = author #'Кэрролл' #input('author: ') --'Кэрролл'
#book['year'] = int(year)#1865 #int(input('year: ')) --'1865'
# print(book)
# L = [1,1,2,3,2]
#
# b = set(L)
#
# print(b)
# # {1,2,3}
# b_list = list(b)
#
# print(b_list)
# # [1,2,3]
# L = input()
# c = list(set(L))
#
# print(len(c))
#
### github
### commit
### time
### back of future
### izi
# # [1,2,3]
# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
#
# debtors = {"Петров", "Антонов"}
#
# non_debtors = abons.difference(debtors)
#
# print(non_debtors)
# # {'Васильев', 'Иванов'}
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# print(a_and_b)
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))
# a = 5
# b = 3+2
# print(id(a))
# print(id(b))
# list_1 = ['a', 'b', 'c']
# list_2 = list_1
# list_3 = list(list_1)
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_1 == list_2)
# print(list_1 == list_3)
# print(list_1 is list_2)
# print(list_1 is list_3)
# L = ['Hello', 'world']
# M = L
#
# print(M is L)
# # True
# M.append('!')
#
# print(L)
# # ['Hello', 'world', '!']
# M = L.copy()
#
# print(M is L)
# # False
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
#
# shopping_center[-1].append("Uniqlo")
#
# print(shopping_center)
# # ('Галерея', 'Санкт-Петербург', 'Лиговский пр., 30', ['H&M', 'Zara', 'Uniqlo'])
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print( list_id_after == list_id_before )
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input("Сумма: "))
# # Возможности языка позволяют выполнить определённые действия для каждого элемента списка map(function, list)
# deposit = list(map(int, list(map((money/100).__mul__, per_cent.values()))))
# # deposit = [int(i * money / 100) for i in per_cent.values()] # Это в следующем модуле
# i = deposit.index(max(deposit))
# print(deposit[i])
# x = input('year: ')
# def is_leap_year(x):
#     return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))
# print(is_leap_year(x = 2000))
# a = [1, 2, 3]
# print(id(a))  # id возвращает идентификатор объекта
# # 140039772293512
#
# b = a
# print(id(b))
# # 140039772293512
#
# print(a is b)  # а и b являются один и тем же объектом
# # True
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b)  # True
# print(a is b)  # False
# a= None
# # Хорошо
# print('is', a is None)
#
# # Плохо
# print('==', a == None)
# is_rainy = True  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")
# mx = 0
# s = 0
# x = int(input())
# if x < 0:
#     s = x
#
# b = 7
# b /= b
#
# if x > mx
#     mx = x
#
# print(s)
# print(mx)
# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")
# print(bool(0))  # False
# print(bool(1))  # True
#
# print(bool("")) # False
# print(bool("1"))  # True
#
# print(bool([])) # False
# print(bool([1]))  # True
# Плохо
# zero = 0
# if zero != 0:
#    print(10 / zero)
# else:
#    print("Делить на ноль нельзя")
#
# # Хорошо
# if zero:
#    print(10 / zero)
# else:
#    print("Делить на ноль нельзя")

# password = input()
# # Плохо
# if password == "":
#    print("Вы забыли ввести пароль")
#
# # Очень плохо
# if len(password) == 0:
#    print("Вы забыли ввести пароль")
#
# # Хорошо
# if not password:
#    print("Вы забыли ввести пароль")

#13.2. Практические примеры с различными операторами
# print(list(str(123456789)))
# # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_digit = list(map(int, list(str(123456789))))
# print(5 in list_digit)
# # True
# print('5' in str(123456789))
# # True
# n = input()
# print('3' in str(n) and '7' in str(n))
# # True

#13.4 Исключения
# print("Перед исключением")
# I = 1 / 0 # Здесь что-то не так….
# print("После исключения")
# print("Перед исключением")
# # теперь пользователь сам вводит числа для деления
# a = int(input("a: "))
# b = int(input("b: "))
# c = a / b # здесь может возникнуть исключение деления на ноль
# print(c) # печатаем c = a / b если всё хорошо
# print(e) # Выводим информацию об ошибке
# print("После исключения")
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")
# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")
# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

# #Задание 13.4.8
# try:
#     n = int(input("Введите число:"))
# except ValueError as e:
#     print("неверное значение")
# else:
#     print("Вы ввели правильное число")
# finally:
#     print("Выход из программы")

# 13.5 Практические примеры с условным оператором
# if A % 2 == 0:
#     print('Число А кратно 2')

# if x > 0:
#     if y > 0:               # x > 0, y > 0
#          print("Первая четверть")
#     else:                   # x > 0, y < 0
#          print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#          print("Вторая четверть")
#     else:                   # x < 0, y < 0
#          print("Третья четверть")
#
# if x > 0 and y > 0:
#     print("Первая четверть")
# if x > 0 and y < 0:
#     print("Четвертая четверть")
# if x < 0 and y > 0:
#     print("Вторая четверть")
# if x < 0 and y < 0:
#     print("Третья четверть")

# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# # username = 'user'
# # password = 'password'
# username = 'user1'
# password = '0123'
# u = username
# p = password
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
# print(check_user(username = u, password = p))

# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# A = int(input('Введите число: '))
# if not (-10 < A < -1 or 2 < A < 10):
#     print("True")
# else:
#     print("False")

# A = int(input('Введите ведите двух значное число: '))
# first_digit = A // 10
# second_digit = A % 10
# print(first_digit, second_digit)
# print((first_digit == 5) or (second_digit == 5))

list_ = [-5, 2, 4, 8, 12, -7, 5]

print(len(list_) == len(set(list_)))