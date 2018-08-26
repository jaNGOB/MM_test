import os
import sys
import ccxt as ccxt

pairs = ['ETH/BTC']

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

exchange = ccxt.poloniex({
    'enableRateLimit': True,
})

orderbook = {}


# -----------------------------------------------------------------------------

def makeOrderbook(orderbook, pairs):
    for pair in pairs:
        pair = ''.join(e for e in pair if e.isalnum())
        orderbook[pair] = {'bids': {'price': 0,
                                    'amount': 0
                                    },
                           'asks': {'price': 0,
                                    'amount': 0}}


def startExchange():
    makeOrderbook(orderbook, pairs)
    while True:
        for symbol in pairs:
            ticker = exchange.fetch_order_book(symbol)
            symbol = ''.join(e for e in symbol if e.isalnum())
            orderbook[symbol]['bids']['price'] = ticker['bids'][0][0]
            orderbook[symbol]['bids']['amount'] = ticker['bids'][0][1]
            orderbook[symbol]['asks']['price'] = ticker['asks'][0][0]
            orderbook[symbol]['asks']['amount'] = ticker['asks'][0][1]
            return orderbook