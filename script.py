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
is_rainy = True  # дождь будет

if is_rainy:
    print("Брать зонт")
else:
    print("Не брать зонт")