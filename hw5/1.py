import requests


class Price:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    @staticmethod
    def _fetch_from_api(from_currency, to_currency) -> dict:
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey=PASTE_YOUR_API_KEY"
        response = requests.get(url)
        return response.json()

    def __add__(self, other):
        if self.currency != other.currency:
            amount_left_in_usd = self.amount / float(Price._fetch_from_api(self.currency, 'USD')['Realtime Currency Exchange Rate']['5. Exchange Rate'])
            amount_right_in_usd = other.amount / float(Price._fetch_from_api(other.currency, 'USD')['Realtime Currency Exchange Rate']['5. Exchange Rate'])
            total_amount_in_usd = amount_left_in_usd + amount_right_in_usd
            total_amount = total_amount_in_usd * float(Price._fetch_from_api('USD', self.currency)['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        else:
            total_amount = self.amount + other.amount

        return Price(total_amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            amount_left_in_usd = self.amount / float(Price._fetch_from_api(self.currency, 'USD')['Realtime Currency Exchange Rate']['5. Exchange Rate'])
            amount_right_in_usd = other.amount / float(Price._fetch_from_api(other.currency, 'USD')['Realtime Currency Exchange Rate']['5. Exchange Rate'])
            total_amount_in_usd = amount_left_in_usd - amount_right_in_usd
            total_amount = total_amount_in_usd * float(Price._fetch_from_api('USD', self.currency)['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        else:
            total_amount = self.amount - other.amount

        return Price(total_amount, self.currency)

    def __repr__(self):
        return f'{self.amount:.2f} {self.currency}'

