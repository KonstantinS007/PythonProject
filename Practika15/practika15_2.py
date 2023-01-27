import json

with open('json_example_QaP.json', encoding='utf8') as f:
    templates = json.load(f)


def CheckInt(item):
    return isinstance(item, int)


def Checkstr(item):
    return isinstance(item, str)


def CheckBool(item):
    return isinstance(item, bool)


def Checkurl(item):
    if isinstance(item, str):
        return item.startswith(‘http: // ') or item.startswith(‘https://")
    else:
         return False

        def CheckStrvalue(item, val):
            if isinstance(item, str):
                return item in val

        else:
        return False

        def ErrorLog(item, value, string):
            Error.append({item: f'{value}, {string}'})

        listofitems = {'timestamp': ‘int’, ‘item_price
        ': ‘int’, ‘referer’: ‘url’, ‘location’: ‘url’, ‘itemurl': ‘url’,
        ‘remoteHost
        ': ‘str’, ‘partyId': ‘str’, ‘sessionId’: ‘str’, ‘pageViewld
        ': ‘str’, ‘itemid': ‘str’,
        “basket_price’: ‘str’, ‘userAgentName
        ': ‘str’, ‘eventType': ‘val’, ‘detectedDuplicate’: ‘bool’,

        ‘detectedcorruption’: ‘bool’, ‘firstInSession’: ‘bool’}

        Error = []
        for items in templates:
            for item in items:
                if item in listofitems:
                    if listofItems[item] == ‘int’:
                    if not CheckInt(items[item]):
                    ErrorLog(item, items[item], ‘ожидали
                тип
                {listofItems[item]}
                ")
                elif listofitems[item] == ‘str’:
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], ‘ожидали
                тип
                {listofItems[item]}
                ")
                elif listofitems[item] == ‘bool’:
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], ‘ожидали
                тип
                {listofItems[item]}
                ")
                elif listofitems[item] == ‘url’:
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], ‘ожидали
                тип
                {listofItems[item]}
                ")
                elif listofitems[item] == ‘val’:
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], ‘ожидали
                значение
                1
                кепвиуЕмепЕ
                или
                itemViewEvent
                ')

                else:
                ErrorLog(item, items[item], ‘HeoxnaanHoe
                3
                HayeHne
                ')
                else:
                ErrorLog(item, items[item], ‘Hew3eectHaa
                переменная‘)

                if Error == []:
                    print(‘pass
                ')
                else:
                print(‘Fail
                ')
                print(Error)
