# Практика 17_9_1 Алгоритмы и структуры данных
# Ввод последовательности чисел
# и нахождение индекса числа после сортировки по возрастанию


def sort_puz(nums):  # Алгоритмом поиска пузырьком
    n = 1
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n += 1
    return nums


def binary_search(array, element, left, right):  # Алгоритм двоичного поиска
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует

        middle = (right + left) // 2  # находимо середину
        if array[middle] == element:  # если элемент в середине,
            return middle - 1  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число не соответствует диапазону'


# Ввод последовательности чисел и преобразование в список
list_vod = input("Введите последовательность натуральных чисел через пробел\nНапример(27 8 4 90 64 32 17 29 33): ")
list_numer = [int(x) for x in list_vod.split()]

# Ввод значения для поиска индекса меньшего числа в пределах диапазона списка
list_min, list_max = min(list_numer), max(list_numer)
vod = True  # Пока не введено число в диапазоне для поиска
numer = 0
while vod:
    numer = input(f'Введите число для определения индекса меньшего введенного в диапазоне ({list_min + 1}-{list_max}):')
    numer = int(numer)
    if not list_min < numer <= list_max:
        print('Число вне диапазона. Повторите ввод.')
    else:
        vod = False

# Сортировка по возрастанию алгоритмом пузырёк
list_numer.append(numer)
list1_hoar = sort_puz(list_numer)
# Вызов алгоритма двоичного поиска и вывод индекса
print("Индекс числа меньшего введенного:", binary_search(list1_hoar, numer, -1, len(list1_hoar) - 1))
