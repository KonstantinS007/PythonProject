# Чтение и запись в файлы
#
# myFile = open('filename.txt', encoding="utf8")
# print(myFile.readlines())
#
#
# # with open('filename.txt', encoding="utf8") as myFile:
# #     for line in myFile:
# #         print(line)
#
#
# # myFile = open('namefile.txt', 'w')
# # myFile.write('KDA')
# # print('POP', file=myFile)
#
# alpha = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЧШЩЫЪЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
# def changeChar(char):
#    if char in alpha:
#        return alpha[(alpha.index(char) + number) % len(alpha) ]
#    elif char in alphaUp:
#        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp) ]
#    else:
#        return char
#
# with open(r"/Task_15/filename.txt", 'rt', encoding="utf8") as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# with open(r"/Task_15/output.txt", 'w', encoding="utf8") as myFile:
#     myFile.write(summary)

# myFile = open('filename.txt')
# myFile = open('filename.txt', 'rt')
myFile = open('filename.txt', 'rt', encoding="utf8")

newfileName = []
with open("newfileName.txt") as myFile:
    for line in myFile:
        newfileName.append(line.replace("\n", ""))

# myFile = open('filename.txt')
print(myFile.read())

print(myFile.readlines())

# for line in myFile:
#     print(line)
#
# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# print('zzzz', file=myFile)
# with open("filename.txt", 'rt', encoding="utf8") as myFile:
#     for line in myFile:
#         print(line)
#
# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
#
# def changeChar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaUp:
#         return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
#     else:
#         return char
#
#
# with open("filename2.txt", encoding="utf8") as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# with open("output.txt", 'w', encoding="utf8") as myFile:
#     myFile.write(summary)
# """Введите
# число, на
# которое
# нужно
# сдвинуть
# текст: 5"""


# def found(pathArr, finPoint):
#     weight = 1
#     for i in range(len(pathArr) * len(pathArr[0])):
#         for y in range(len(pathArr)):
#             for x in range(len(pathArr[y])):
#                 if pathArr[y][x] == weight:
#                     # Вниз
#                     if y > 0 and pathArr[y - 1][x] == 0:
#                         pathArr[y - 1][x] = weight + 1
#
#                         # Вверх
#                     if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
#                         pathArr[y + 1][x] = weight + 1
#
#                     # Вправо
#                     if x > 0 and pathArr[y][x - 1] == 0:
#                         pathArr[y][x - 1] = weight + 1
#
#                     # Влево
#                     if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
#                         pathArr[y][x + 1] = weight + 1
#
#                     # Конечная точка
#                     if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
#                         pathArr[finPoint[0]][finPoint[1]] = weight + 1
#                         return True
#         weight += 1
#     return False
#
#
# def printPath(pathArr, finPoint):
#     y = finPoint[0]
#     x = finPoint[1]
#     weight = pathArr[y][x]
#     result = list(range(weight))
#     while (weight):
#         weight -= 1
#         if y > 0 and pathArr[y - 1][x] == weight:
#             result[weight] = 'Вниз'
#             y -= 1
#         elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
#             result[weight] = 'Вверх'
#             y += 1
#         elif x > 0 and pathArr[y][x - 1] == weight:
#             result[weight] = 'Вправо'
#             x -= 1
#         elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
#             result[weight] = 'Влево'
#             x += 1
#
#     return result[1:]
#
#
# labirint = []
# with open("labirint.txt") as myFile:
#     for line in myFile:
#         labirint.append(line.replace('\n', '').split(' '))
#
# ii = 0
# for i in labirint:
#     jj = 0
#     for j in i:
#         if j == 'A':
#             labirint[ii][jj] = 1
#             pozIn = (ii, jj)
#         elif j == 'B':
#             labirint[ii][jj] = 0
#             pozOut = (ii, jj)
#         elif j == '1':
#             labirint[ii][jj] = -1
#         else:
#             labirint[ii][jj] = 0
#         jj += 1
#     ii += 1
#
# if not found(labirint, pozOut):
#     print("Путь не найден!")
# else:
#     result = printPath(labirint, pozOut)
#
#     for i in labirint:
#         for line in i:
#             print("{:^3}".format(line), end=" ")
#         print()
#     print(result)