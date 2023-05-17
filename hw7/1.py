import requests
import httpx
import asyncio
import tracemalloc

tracemalloc.start()

class Price:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    @staticmethod
    async def _fetch_from_api(from_currency, to_currency) -> dict:
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey=D2HNG6677IVG9UDS"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response.json()

    async def _fetch_exchange_rate(self, from_currency, to_currency):
        response = await Price._fetch_from_api(from_currency, to_currency)
        return float(response.get('Realtime Currency Exchange Rate', {}).get('5. Exchange Rate', 1))

    async def __add__(self, other):
        if self.currency != other.currency:
            exchange_rate_left = await self._fetch_exchange_rate(self.currency, 'USD')
            exchange_rate_right = await self._fetch_exchange_rate(other.currency, 'USD')
            amount_left_in_usd = self.amount / exchange_rate_left
            amount_right_in_usd = other.amount / exchange_rate_right
            total_amount_in_usd = amount_left_in_usd + amount_right_in_usd
            total_amount = total_amount_in_usd * await self._fetch_exchange_rate('USD', self.currency)
        else:
            total_amount = self.amount + other.amount

        return Price(total_amount, self.currency)

    async def __sub__(self, other):
        if self.currency != other.currency:
            exchange_rate_left = await self._fetch_exchange_rate(self.currency, 'USD')
            exchange_rate_right = await self._fetch_exchange_rate(other.currency, 'USD')
            amount_left_in_usd = self.amount / exchange_rate_left
            amount_right_in_usd = other.amount / exchange_rate_right
            total_amount_in_usd = amount_left_in_usd - amount_right_in_usd
            total_amount = total_amount_in_usd * await self._fetch_exchange_rate('USD', self.currency)
        else:
            total_amount = self.amount - other.amount

        return Price(total_amount, self.currency)

    def __repr__(self):
        return f'{self.amount:.2f} {self.currency}'


async def main():
    price1 = Price(10, 'USD')
    price2 = Price(10, 'UAH')

    while True:
        result = await price1.__add__(price2)
        print(result)
        await asyncio.sleep(10)

asyncio.run(main())