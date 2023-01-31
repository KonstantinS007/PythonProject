# class Bird:
#     def __init__(self):
#         print('птица готова')
#
#     def whoisThis(self):
#         print('птица')
#
#     def swim(self):
#         print('плывет быстрее')
#
#
# # дочерний класс
# class Penguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print('пингвин готов')
#
#     def whoisThis(self):
#         print('пингвин')
#
#     def run(self):
#         print('бежит быстрее')
#
# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()

# class Computer:
#     def __init__(self):
#         self.__maxprice = 900
#
#     def sell(self):
#         print(f'цена продажи {self.__maxprice}')
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# c = Computer()
# c.sell()
#
# c.__maxprice = 1000
# c.sell()
#
# c.setMaxPrice(1000)
# c.sell()

# полимотфизм
# позволяет использовать функцию для разных форм (типы данных)

# Import time module
import time
import math
# record start time
start = time.time()

# define a sample code segment
n = 10000
n = n ^ 2
print(n)

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end - start) * 1000 ** 10, "ms")

# record start time
start = time.time()

# define a sample code segment
n = 10000
n = n * math.log(n, 2)
print(n)

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end - start) * 1000 ** 10, "ms")
n = 10000
n = round(n / math.log(n, 2))
print(n)

