#           EXTENSIONS.PY
import requests
import json
from Practice_18.TeleBOT.config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')#.json()
        #  total_base = r[base_ticker] * float(amount) # ←-----------можно вот так, без#---------------------------↑
        total_base = json.loads(r.content)[keys[base]] * float(amount)  # ←--а вот это #
        total_base = round(total_base, 2)
        return total_base
