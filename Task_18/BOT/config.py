#         CONFIG.PY
# import requests
# import json
with open('../../../Cat.txt', 'r') as f:
    cat = f.read()
TOKEN = cat

TIMEZONE = 'MOSKVA'
TIMEZONE_COMMON_NAME = 'MOSKVA'

keys = {
      'рубль': 'RUR',
      'доллар': 'USD',
      'евро': 'EUR',
}
