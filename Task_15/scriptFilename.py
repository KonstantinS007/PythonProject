# Чтение и запись в файлы
#
# myFile = open('filename.txt', encoding="utf8")
# print(myFile.readlines())


# with open('filename.txt', encoding="utf8") as myFile:
#     for line in myFile:
#         print(line)


# myFile = open('namefile.txt', 'w')
# myFile.write('KDA')
# print('POP', file=myFile)

alpha = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЧШЩЫЪЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''

def changeChar(char):
   if char in alpha:
       return alpha[(alpha.index(char) + number) % len(alpha) ]
   elif char in alphaUp:
       return alphaUp[(alphaUp.index(char) + number) % len(alphaUp) ]
   else:
       return char

with open("filename.txt", 'rt', encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w', encoding="utf8") as myFile:
    myFile.write(summary)

