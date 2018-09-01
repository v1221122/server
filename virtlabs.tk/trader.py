import sys
import http.client
import urllib
import json
import hashlib
import hmac
import time
import requests

def get_highest_price(ask):
    best = ask[0][0]
    for a in ask:
        if best < a[0]:
            best = a[0]
    return best

def get_lowest_price(ask):
    best = ask[0][0]
    for a in ask:
        if best > a[0]:
            best = a[0]
    return best

def get_prices():
    r = requests.get('https://api.exmo.com/v1/order_book?pair=LTC_BTC')
    return r.json()['LTC_BTC']

class ExmoAPI:
    def __init__(self, API_KEY, API_SECRET, API_URL = 'api.exmo.com', API_VERSION = 'v1'):
        self.API_URL = API_URL
        self.API_VERSION = API_VERSION
        self.API_KEY = API_KEY
        self.API_SECRET = bytes(API_SECRET, encoding='utf-8')
        self.nonce = int(time.time() * 1000)
        self.btc_balance = 0.00050614
        self.ltc_balance = 0.05890065
        print(self.nonce)

    def sha512(self, data):
        H = hmac.new(key = self.API_SECRET, digestmod = hashlib.sha512)
        H.update(data.encode('utf-8'))
        return H.hexdigest()

    def api_query(self, api_method, params = {}):
        params['nonce'] = self.nonce
        self.nonce += 1
        params =  urllib.parse.urlencode(params)

        sign = self.sha512(params)
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Key": self.API_KEY,
            "Sign": sign
        }
        conn = http.client.HTTPSConnection(self.API_URL)
        conn.request("POST", "/" + self.API_VERSION + "/" + api_method, params, headers)
        response = conn.getresponse().read()

        conn.close()

        try:
            obj = json.loads(response.decode('utf-8'))
            if 'error' in obj and obj['error']:
                print(obj['error'])
                raise sys.exit()
            return obj
        except json.decoder.JSONDecodeError:
            print('Error while parsing response:', response)
            raise sys.exit()

# Example
api = ExmoAPI(
                            'K-b90680b171c69ac996a55a2066f8d38d0a50b9d4',
                            'S-7c2e02d07fd2dab84eef46e0606dc0f6e7e9173a'
)
while True:
    prices = get_prices()
    balances = api.api_query('user_info')['balances']
    print('LTC: ', balances['LTC'], '  BTC: ', balances['BTC'])
    highest_price = get_highest_price(prices['bid'])
    lowest_price = get_lowest_price(prices['ask'])
    print('sell: ', highest_price, 'buy: ', lowest_price)
    if float(balances['LTC']) > .04:
        print(
              'amount_btc: ',
              float(balances['LTC']) * float(highest_price) * .99,
              ' cur_balance:',
              api.btc_balance,
              '\n'
        )
    if float(balances['BTC']) > .0004:
        print(
              'amount_ltc: ',
              '{:.9f}'.format(float(balances['BTC']) / float(lowest_price) * .99),
              ' cur_balance:',
              api.ltc_balance,
              '\n'
        )
    if float(balances['LTC']) * float(highest_price) * .99 > api.btc_balance:
        api.api_query(
                'order_create',
                {
                    'pair': 'LTC_BTC',
                    'quantity': balances['LTC'],
                    'price': highest_price,
                    'type': 'sell'
        })
        print('selled ', balances['LTC'], '  price: ', highest_price, '\n')
        api.btc_balance = float(balances['LTC']) * float(highest_price)
    if float(balances['BTC']) / float(lowest_price) * .99 > api.ltc_balance:
        api.api_query(
                'order_create',
                {
                    'pair': 'LTC_BTC',
                    'quantity': balances['BTC'],
                    'price': lowest_price,
                    'type': 'buy'
        })
        print('bought ', balances['BTC'], '  price: ', lowest_price, '\n')
        api.ltc_balance = float(balances['BTC']) / float(lowest_price)
    time.sleep(1)
