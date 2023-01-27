import json

with open('json_example_QaP.json', encoding='utf8') as f:
    templates = json.load(f)


def check_int(item1):
    return isinstance(item1, int)


def check_str(item1):
    return isinstance(item1, str)


def check_bool(item1):
    return isinstance(item1, bool)


def check_url(item1):
    if isinstance(item1, str):
        return item1.startswith('http: // ') or item1.startswith('https://')
    else:
        return False


def check_str_value(item1, val):
    if isinstance(item1, str):
        return item1 in val
    else:
        return False


def error_log(item1, value, string):
    Error.append({item1: f'{value}, {string}'})


Error = []
listofitems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'itemurl': 'url',
               'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewld': 'str', 'icate': 'bool',
               'detectedcorruption': 'bool', 'firstInSession': 'bool'}

for items in templates:
    for item in items:
        if item in listofitems:
            if listofitems[item] == 'int':
                if not check_int(items[item]):
                    error_log(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'str':
                    if not check_str(items[item]):
                        error_log(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'bool':
                    if not check_bool(items[item]):
                        error_log(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'url':
                    if not check_url(items[item]):
                        error_log(item, items[item], f'ожидали тип {listofitems[item]}')
                elif listofitems[item] == 'val':
                    if not check_str_value(items[item], ['itemBuyEvent', 'itemViewEvent']):
                        error_log(item, items[item], 'ожидали значения itemBuyEvent или itemViewEvent')
                else:
                    error_log(item, items[item], 'Неожиданное значение')
            else:
                error_log(item, items[item], 'Неизвестная переменная')

if Error is []:
    print('pass')
else:
    print('Fail')
    print(Error)
