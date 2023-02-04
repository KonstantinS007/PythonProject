# import requests
#
# r = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
# print(r.content)
# print(r.status_code)
# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
# print(r.content)

# import requests
# import json  # импортируем необходимую библиотеку

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')
#
# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# print(r.content)

# import requests
# import json
#
# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(
#     data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)

# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#
# r = json.loads(r.content)
#
# print(r[0])

# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
#
# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath(
#     '/html/head/title/text()')
# # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге
# # <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.
# print(title)  # выводим полученный заголовок страницы

import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall(
    '//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл? в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    t = li.find('time')
    print(a.text)  # из этого тега забираем текст — это и будет нашим названием
    print(t.get('datetime'))
