# Task 17

# def p(n):
#     if n == 0:
#         return
#     else:
#         p(n-1)
#         print(n)
#
#
# p(5)

# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
#
#
# print(par_checker('(5+6)*(7+8)/(4+3)'))

pars = {")": "(", "]": "["}


# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
#
# print(par_checker('(5+6)*(7+8)/(4+3)'))

N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

def is_empty():
    return head == tail and queue[head] == 0


def size():
    if is_empty():
        return 0
    elif head == tail:
        return N_max
    elif head > tail:
        return N_max - head + tail
    else:
        return tail - head

def add():
    global tail, order
    order += 1
    queue[tail] = order
    print("Задача №%d добавлена" % (queue[tail]))

    tail = (tail + 1) % N_max


def show():
    print("Задача №%d в приоритете" % (queue[head]))


def do():
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0
    head = (head + 1) % N_max


while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

