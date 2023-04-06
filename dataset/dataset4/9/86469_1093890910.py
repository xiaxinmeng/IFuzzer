from binance.client import Client
from binance.exceptions import *

client = Client(api_key='Your_Public_Apikey',
                api_secret='Your_Secret_Apikey')

def buy_limit_test(coin, amount):
    client.create_test_order(
        symbol=coin + 'USDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=amount)