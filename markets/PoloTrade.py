import time
import ccxt as ccxt

pairs = ['ETH/BTC']

exchange = ccxt.poloniex({
    'apiKey': '',
    'secret': '',
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


def fetchOB(symbol):
    try:
        ticker = exchange.fetch_order_book(symbol)
        return ticker

    except (ccxt.ExchangeError, ccxt.AuthenticationError, ccxt.ExchangeNotAvailable, ccxt.RequestTimeout) as error:
        print('Got an error', type(error).__name__, error.args, ', retrying in 30 seconds...')
        time.sleep(30)
        fetchOB(symbol)


def createorder(side, amount, symbol):
    try:
        exchange.create_order(symbol, 'market', side, amount)
    except (ccxt.ExchangeError, ccxt.AuthenticationError, ccxt.ExchangeNotAvailable, ccxt.RequestTimeout) as error:
        print('Got an error', type(error).__name__, error.args, ', retrying in 30 seconds...')
        time.sleep(30)
        createorder(side, amount, symbol)


def getBalance():
    try:
        return exchange.fetch_balance()
    except (ccxt.ExchangeError, ccxt.AuthenticationError, ccxt.ExchangeNotAvailable, ccxt.RequestTimeout) as error:
        print('Got an error', type(error).__name__, error.args, ', retrying in 30 seconds...')
        time.sleep(30)
        getBalance()


def startExchange():
    makeOrderbook(orderbook, pairs)
    while True:
        for symbol in pairs:
            ticker = fetchOB(symbol)
            symbol = ''.join(e for e in symbol if e.isalnum())
            orderbook[symbol]['bids']['price'] = ticker['bids'][0][0]
            orderbook[symbol]['bids']['amount'] = ticker['bids'][0][1]
            orderbook[symbol]['asks']['price'] = ticker['asks'][0][0]
            orderbook[symbol]['asks']['amount'] = ticker['asks'][0][1]
            return orderbook