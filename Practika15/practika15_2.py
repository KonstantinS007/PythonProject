import json

with open('json_example_QaP.json', encoding='utf8') as f:
    templates = json.load(f)


def Check_Int(item):
    return isinstance(item, int)


def Check_str(item):
    return isinstance(item, str)


def Check_Bool(item):
    return isinstance(item, bool)


def Check_url(item):
    if isinstance(item, str):
        return item.startswith('http: // ') or item.startswith('https://')
    else:
        return False


def Check_Strvalue(item, val):
    if isinstance(item, str):
        return item in val

    else:
        return False


def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})


Error = []
listofitems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'itemurl': 'url',
               'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewld': 'str', 'icate': 'bool',
               'detectedcorruption': 'bool', 'firstInSession': 'bool'}

for items in templates:
    for item in items:
        if item in listofitems:
            if listofitems[item] == 'int':
                if not Check_Int(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'str':
                    if not Check_str(items[item]):
                        ErrorLog(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'bool':
                    if not Check_Bool(items[item]):
                        ErrorLog(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'url':
                    if not Check_url(items[item]):
                        ErrorLog(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'val':
                    if not Check_Strvalue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                        ErrorLog(item, items[item], 'ожидали значения itemBuyEvent или itemViewEvent')
                else:
                    ErrorLog(item, items[item], 'HeoxnaanHo 3 HayeHnу')
            else:
                ErrorLog(item, items[item], 'Неизвестная переменная')

if Error == []:
    print('pass')
else:
    print('Fail')
    print(Error)
