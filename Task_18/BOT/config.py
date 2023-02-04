#         CONFIG.PY
# import requests
# import json
with open('../../../Cat.txt', 'r') as f:
    cat = f.read()
TOKEN = cat

TIMEZONE = 'MOSKVA'
TIMEZONE_COMMON_NAME = 'MOSKVA'

keys = {
      'рубль': 'RUB',
      'доллар': 'USD',
      'евро': 'EUR',
}
