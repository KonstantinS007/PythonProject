import json

with open('json_example_QaP.json', encoding='utf8') as f:
    templates = json.load(f)


def check_int(ite):
    """Возращяет true если в поле целое число"""
    return isinstance(ite, int)


def check_str(ite):
    """Возращяет true если в поле строка"""
    return isinstance(ite, str)


def check_bool(ite):
    """Возращяет true если в поле bool"""
    return isinstance(ite, bool)


def check_url(ite):
    """Возращяет true если в поле строка и имеет наччало http:// или https://"""
    if isinstance(ite, str):
        return ite.startswith('http://') or ite.startswith('https://')
    else:
        return False


def check_str_value(ite, val):
    """Возращяет true если в поле itemBuyEvent или itemViewEvent"""
    if isinstance(ite, str):
        return ite in val
    else:
        return False


def error_log(ite, value, string):
    """Записывает неправильные поля и значения"""
    Error.append({ite: f'{value}, {string}'})


Error = []
listofitems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url',
               'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'item_id': 'str',
               'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool',
               'icate': 'bool', 'detectedCorruption': 'bool', 'firstInSession': 'bool'}

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
            error_log(item, items[item], 'Неизвестное поле')

if not Error:
    print('Pass')
else:
    print('Fail')
    print(Error)
