#  Задание 12.7.3 (HW-03)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма: "))

# map(function, list) позволят выполнить определённые действия для каждого элемента списка
# ().__mul__ умножение элементов, получения списка значений полученых накоплений в каждом банке
# deposit = list(map(int, list(map((money/100).__mul__, per_cent.values()))))

deposit = list(map(lambda x: int(x*money/100), per_cent.values()))

# это в следующем модуле
# deposit = [int(i * money / 100) for i in per_cent.values()]

# находим максимальное значение и его индекс в списке
i = deposit.index(max(deposit))
print(deposit[i])
