def change_Text(text):
    """
    Функция принимает строку с текстом.
    Убирает все знаки препинания и возвращает
    список, состоящий из слов текста.
    """

    for i in r'!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')

    return text.split()



def most_Common(text, length=0):
    """
    Функция принимает список и ограничение по длине.
    Возвращает самый часто встречающийся элемент.
    Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
    """

    most_common = []
    qty_most_common = 0

    for item in text:
        if len(item) > length:
            qty = text.count(item)
            if qty > qty_most_common and qty > 2:
                qty_most_common = qty
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)

    return list(set(most_common))


def most_Length(text):
    """
    Функция принимает список.
    Возвращает самый длинный элемент.
    Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
    """

    most_length = []
    qty_most_length = 0
    alphabet = r'abcdefghijklmnopqrstuvwxyz`ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for char in item:
            if char not in alphabet:
                charEn = False
            else:
                charEn = True

            if charEn:
                qty = len(item)
                if qty > qty_most_length:
                    qty_most_length = qty
                    most_length = [item]
                elif qty == qty_most_length:
                    most_length.append(item)

    return list(set(most_length))


nameFile = input('Название файла ' + '(text1.txt): ')

with open(nameFile, encoding='utf8') as f:
    fileText = f.read()


fileText = change_Text(fileText)
print(len(fileText))
print(f'Список самых частых слов длинной более трёх символов: {most_Common(fileText, 3)}')
print(f'Список самых длинных английских слов: {most_Length(fileText)}')

help(change_Text)
help(most_Common)
help(most_Length)
