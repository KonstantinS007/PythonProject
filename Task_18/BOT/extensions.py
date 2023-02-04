#           EXTENSIONS.PY
import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
            text = f'<Невозможно перевести одинаковые валюты> '
            bot.send_message(message.chat.id, text)
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
            text = '\n <Не удалось обработать переводимую валюту> '
            bot.send_message(message.chat.id, text)
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
            text = '\n <Не удалось обработать валюту>'
            bot.send_message(message.chat.id, text)
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
            text = '\n Не удалось обработать количество'
            bot.send_message(message.chat.id, text)
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}').json()
        total_base = json.loads(r.content)[keys[base]]
        return total_base
