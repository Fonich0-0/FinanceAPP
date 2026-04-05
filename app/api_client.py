import requests


class Converter:
    """Конвертер в одну строку"""
    @staticmethod
    def convert(amount, from_curr, to_curr):
        url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
        rate = requests.get(url).json()['rates'][to_curr]
        return round(amount * rate, 2)

result = Converter.convert(100, 'USD', 'RUB')
print(result)