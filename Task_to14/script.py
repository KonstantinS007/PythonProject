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
# print(list(map(float, L)))
# string = input("Введите числа через пробел:1 1 2 3 5 8 13 21 34 55")
#
# list_of_strings = string.split() # список строковых представлений чисел
# print(list_of_strings) # вывод списка чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
# list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]
# # print(sum(list_of_numbers[::3]))
# list_sum = sum(list_of_numbers)
# list_of_numbers.append(list_sum)
# print(list_of_numbers)
# # 1 1 2 3 5 8 13 21 34 55
# # все операции - деление строки по пробелам, преобразование к числам
# # и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(float, input("Введите :").split()))
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
# book = {}
# book['title'] = title #'Алиса в стране чудес' #input('title: ') --'Алиса в стране чудес'
# book['author'] = author #'Кэрролл' #input('author: ') --'Кэрролл'
# book['year'] = int(year)#1865 #int(input('year: ')) --'1865'
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
# ## github
# ## commit
# ## time
# ## back of future
# ## izi
# # [1,2,3]
# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
#
# debtors = {"Петров", "Антонов"}
#
# non_debtors = abons.difference(debtors)
#
# print(non_debtors)
# # {'Васильев', 'Иванов'}
a = '1 2 3 4 5 6 7 8'  # input("Введите первую строку: ")
b = '2 4 6 8 10 12'  # input("Введите вторую строку: ")
print(type(a))
print(b)
a = a.split(' ')
b = b.split(' ')

print(b)
a_set = set(a)  # используем множественное присваивание
b_set = set(b)
print(a_set)
print(b_set)

a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)
print(type(a_and_b))

a_and_b = str(sorted(map(int, list(a_and_b))))

a_and_b = a_and_b.replace(',', "")
print(a_and_b)
print(type(a_and_b))

# my_list = [3]
#
# my_set_1 = set('1, 2, 3')
# my_set_2 = set('2, 3, 4')
# my_set_3 = set(my_list)
# print(my_set_1)
# print(my_set_2)
# print(my_set_3)
# a = my_set_1.symmetric_difference(my_set_2)  # {1, 4}
#  # {1, 4}
# print(a)
# a = my_set_1.symmetric_difference(my_list)  # {1, 2}
#   # TypeError
# print(a)









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

# 13.2. Практические примеры с различными операторами
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

# 13.4 Исключения
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
# else:  # код в блоке else выполняется только в том случае,
# если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
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

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# num = 123456787654321
#
# print(str(num) == str(num)[::-1])

# 13.6 Циклы
#
#
# time = 0
# while (true) do
# {
#     wait(1)
#     print(time)
# }

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)
#
# P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение, подумайте чему она должна быть равна
# N = 5
#
# for i in range(1, N+1):
#     P *= i
#
# print(P)

# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# хорошо
# #
# n = 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#    print("Hello World")
#    n += 1
#    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
#        break
#

# n = 1
#
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1

# N = 2
# M = 3
# заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#
#
# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
# 0 1 2 3 4 5
# N = 2
# M = 3
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end=" ")
#     print()  # перенос на новую строку
#
# # 0 1 2
# # 3 4 5

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)
#
# 13.7 Практические примеры

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """

# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
#
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
#
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# n = int(input())
#
# while True:
#     if n % 3 == 0:
#          n = n // 3
#          if n == 1:
#               break
#     else:
#          break
#
# n = 3

# def print_ladder(n):
#     for i in range(1,n+1):
#         print('*' * i)
#

# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# a = '' # пустая строка
# b = a or 1
# print(b)
#
# a = "foo"
# b = "bar"
#
# print(1 and a or b)
#
# a = ""
# b = "bar"
#
# print(1 and a or b)
#
# # пусть a и b - переменные, которые мы хотим проверитьif ??? : # проверка истинности обеих переменных
#     print("Обе переменные истинные")
#     print(a,b)
# a = int(input())
# if type(a) == int:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Число удовлетворяет условиям")
#     else:
#         print("false")
# a = int(input())
# if type(a) == int:
#     if 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#         print("Число удовлетворяет условиям")
#     else:
#         print("false")
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")


# L = list(map(int, input().split()))
#
# print(all(L))

# L = list(map(int, input().split()))
#
# print(not any(L))

# list_tuples = [(i, i**2) for i in range(1,11)]
# print(list_tuples,'\n')

# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)

# L = [int(input()) % 2 == 0 for i in range(5)]
# print( any(L))


# B = int(input('Количество билетов: '))
# n = 0
# for i in range(1, B+1):
#     s = int(input('Возраст: '))
#     if 18 <= s <25:
#         n += 990
#     if s >= 25:
#         n += 1390
# if B >= 3:
#     n = n - n/10
# print('Сумма к оплате: ',n,'руб.')

# Proverka chujogo koda
# money = float(input('Ввести сумму:'))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# deposit = []
# deposit.append(money*5.6/100)
# deposit.append(money*5.9/100)
# deposit.append(money*4.28/100)
# deposit.append(money*4/100)
# print(deposit)
#
# print('Максимальная сумма, которую вы можете заработать', max(deposit))

# print(str(123456789)), print('3' and '7' in str(123456789))

# modul 14.1

# объявили функцию для подсчета количества символов в тексте


# def char_frequency():
#    text = """
#    У лукоморья дуб зелёный;
#    Златая цепь на дубе том:
#    И днём и ночью кот учёный
#    Всё ходит по цепи кругом;
#    Идёт направо -- песнь заводит,
#    Налево -- сказку говорит.
#    Там чудеса: там леший бродит,
#    Русалка на ветвях сидит;
#    Там на неведомых дорожках
#    Следы невиданных зверей;
#    Избушка там на курьих ножках
#    Стоит без окон, без дверей;
#    Там лес и дол видений полны;
#    Там о заре прихлынут волны
#    На брег песчаный и пустой,
#    И тридцать витязей прекрасных
#    Чредой из вод выходят ясных,
#    И с ними дядька их морской;
#    Там королевич мимоходом
#    Пленяет грозного царя;
#    Там в облаках перед народом
#    Через леса, через моря
#    Колдун несёт богатыря;
#    В темнице там царевна тужит,
#    А бурый волк ей верно служит;
#    Там ступа с Бабою Ягой
#    Идёт, бредёт сама собой,
#    Там царь Кащей над златом чахнет;
#    Там русский дух... там Русью пахнет!
#    И там я был, и мёд я пил;
#    У моря видел дуб зелёный;
#    Под ним сидел, и кот учёный
#    Свои мне сказки говорил.
#    """
#
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
#
# ...
#
# # вызвали функцию в любом месте программы
# char_frequency()

# def print_2_add_2():
#    result = 2 + 2
#    print(result)
#
# print_2_add_2()

# def hello_world():
#    print("Hello World")
#
# hello_world()

# объявили функцию для подсчета количества символов в неком абстрактном тексте
# def char_frequency(text):
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")


# # функция, которая возводит любое число в квадрат
# def pow_func(base):
#    print(base ** 2)
#
# pow_func(3)  # 9
# pow_func(5)  # 25

# # функция, которая возводит любое число в степень n
# def pow_func(base, n=2):
#    print(base ** n)
#
# pow_func(3)  # 9
# pow_func(5, 3)  # 125

#
# def check_num(a, n):
#    if a % n == 0:
#        print(f"Число {n} является делителем числа {a}")
#    else:
#        print(f"Число {n} не является делителем числа {a}")
#
# check_num(4, 2)  # Число 2 является делителем числа 4
# check_num(5, 2)  # Число 2 не является делителем числа 5


# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
# n = int(input())
# reverse_stair(n)

# def pow_func(base, n=2):
# #    print(base ** n)
# #
# # print(pow_func(3))

# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))
# # 9

# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# print(get_multipliers(5))  # 2
# print(get_multipliers(4))  # 3


# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# print(check_palindrome("test"))  # False
# print(check_palindrome("Кит на море не романтик"))  # True

# x = 3
#
#
# def func():
#    global x  # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
# func()
# print(x)

# def get_my_func():
#
#     def hello_world():
#         print("Hello")
#
#     return hello_world
#
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()  # Hello

# def get_mul_func(m):
#     nonlocal_m = m
#
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(5))  # 5 * 2

# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6

# def mul(*nums):
#     p = 1
#     for n in nums:
#         p *= n
#
#     return p

# def rec_fibb(n):
#
#    if n == 1:
#        return 1
#
#    if n == 2:
#       return 1
#
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
#
# print(rec_fibb(10))  # 55

# def summ_n(n):
#     if n == 1:
#          return 1
#     return n + summ_n(n - 1)
# print(summ_n(10))

# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# print(reverse_str('test'))  # tset

# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# print(sum_digit(123))  # 6

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
# print(count(5,2))

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)


# def make_adder(x):
#
#     def adder(n):
#         return x + n  # захват переменной "x" из nonlocal области
#
#     return adder  # возвращение функции в качестве результата
#
#
# # функция, которая будет к любому числу прибавлять пятёрку
# add_5 = make_adder(5)
#
# print(add_5(10))  # 15
# print(add_5(100))  # 105

# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
#
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0


# import time


# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2


# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
#
# in_build_pow()
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458


# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)

# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")


# def my_decorator(fn):
#    def wrapper():
#        fn()
#    return wrapper  # возвращается задекорированная функция, которая заменяет исходную
#
# # выведем незадекорированную функцию
# def my_function():
#    pass
# print(my_function)  # <function my_function at 0x7f938401ba60>
#
# # выведем задекорированную функцию
# @my_decorator
# def my_function():
#    pass
# print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>


# декоратор, в котором встроенная функция умеет принимать аргументы
# def do_it_twice(func):

#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
#
# @do_it_twice
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Oo!!!


# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper

# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз


# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper


# def linear_solve(a, b):
#     return b/a
# # 2*x = 9
# print(linear_solve(2, 9))
# # 0*x = 1
# print(linear_solve(0,1))


# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
#
# print(linear_solve(0,0))


# def diskriminant(a,b,c):
#    def quadratic_solve(a,b,c):
#       if diskriminant(a,b,c) < 0:
#         return "Нет вещественных корней"
#       elif diskriminant(a,b,c) == 0:
#           return -b / (2 * a)
#       else:
#           return (-b - diskriminant(a, b, c) ** 0.5) / (2 * a), (-b + diskriminant(a, b, c) ** 0.5) / (2 * a)
#
# # разбили строку из input и преобразовали к float
# # Ввод строки 1 0 -1
# L = list(map(float, input().split()))
# # Вывод [1.0, 0.0, -1.0]
# # [1, 0, -1] - например
# print(quadratic_solve(L[0], L[1], L[2]))
# # (-1.0, 1.0)


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)


# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)


# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# Из заданного списка вывести только положительные элементы
# def positive(x):
#     return x % 2 == 0  # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]


# a = ["asd", "bbd", "ddfa", "mcsa"]
# print(list(map(lambda x: len(x), a)))


# #  Задание 12.7.3 (HW-03)
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input("Сумма: "))
#
# # map(function, list) позволят выполнить определённые действия для каждого элемента списка
# # ().__mul__ умножение элементов, получения списка значений полученых накоплений в каждом банке
# # deposit = list(map(int, list(map((money/100).__mul__, per_cent.values()))))
#
# deposit = list(map(lambda x: int(x*money/100), per_cent.values()))
#
# # это в следующем модуле
# # deposit = [int(v * money / 100) for v in per_cent.values()]
#
# # находим максимальное значение и его индекс в списке
# i = deposit.index(max(deposit))
# print(deposit[i])

# n = {'wer': 'we', 'cc': 'ee'}
# print(type(n))
