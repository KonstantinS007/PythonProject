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
n = 3

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
