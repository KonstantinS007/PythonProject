# ЗАДАНИЕ 13.8.19 (HW-03)

# B = int(input('Количество билетов: '))
# n = 0
# for i in range(1, B+1):
#     s = int(input('Возраст: '))
#     if 18 <= s <25: # с 18 до 25
#         n += 990
#     if s >= 25: # от 25 и старше
#         n += 1390
# if B > 3: # Скидка на стоимость 10% более 3 посетителей
#     n = n - n/10
# print('Сумма к оплате: ',n,'руб.')


ticket = int(input('Количество билетов: '))
summa = 0
skidka, registr = 10, 3  # процент и условие более зарегестрированых
person = 0

for person in range(1, ticket+1):
    age_person = int(input(f'Возраст посетителя для билета - {person}: '))
    if 18 <= age_person < 25:  # с 18 до 25
        summa += 990
    elif age_person >= 25:  # от 25 и старше
        summa += 1390


if ticket > registr:  # Скидка на стоимость 10% более 3 посетителей
    summa = summa-summa/100*skidka
    print('Скидка: ', skidka, '% Более', registr, 'зарегистрированных.')

print('Количество зарегистрированых: ', person)
print('Сумма к оплате: ', summa, 'руб.')
