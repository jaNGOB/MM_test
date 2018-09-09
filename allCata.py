import numpy as np
import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
from catalyst import run_algorithm
from catalyst.api import (
    record,
    order,
    order_target_percent,
    symbol,
    get_order
)
from logbook import Logger

log = Logger("Arbitrage")


def initialize(context):
    log.info('initializing pairs trading algorithm')
    context.bitfinex = context.exchanges['bitfinex']
    context.poloniex = context.exchanges['poloniex']

    context.bitfinex_trading_pair = symbol('btc_usd', context.bitfinex.name)
    context.poloniex_trading_pair = symbol('btc_usdt', context.poloniex.name)

    context.swallow_errors = True
    context.errors = []

    context.threshold = 20

    context.longBfx = False
    context.longPolo = False


def _handle_data(context, data):
    poloniex_price = data.current(context.poloniex_trading_pair, 'close')
    bitfinex_price = data.current(context.bitfinex_trading_pair, 'close')

    if poloniex_price > bitfinex_price:
        biggerPolo = poloniex_price - bitfinex_price
        if biggerPolo > context.threshold and not context.longPolo:
            longPolo(context)
            log.info('Short Polo at {polo_price} and long Finex at {finex_price}'.format(polo_price=poloniex_price,
                                                                                         finex_price=bitfinex_price))
        else:
            log.info('no opportunity found')

    elif bitfinex_price > poloniex_price and not context.longBfx:
        biggerBfx = bitfinex_price - poloniex_price
        if biggerBfx > context.threshold:
            longBfx(context)
            log.info('Short Finex at {finex_price} and long Polo at {polo_price}'.format(polo_price=poloniex_price,
                                                                                         finex_price=bitfinex_price))
        else:
            log.info('no opportunity found')

    else:
        log.info('no opportunity found')


def handle_data(context, data):
    # log.info('----------------------------------------------------------')
    try:
        _handle_data(context, data)
    except Exception as e:
        log.warn('aborting the bar on error {}'.format(e))
        context.errors.append(e)

    # log.info('completed bar {}, total execution errors {}'.format(data.current_dt, len(context.errors)))

    if len(context.errors) > 0:
        log.info('the errors:\n{}'.format(context.errors))


def longBfx(context):
    order_target_percent(context.poloniex_trading_pair, -0.5)
    order_target_percent(context.bitfinex_trading_pair, 0.5)
    context.longBfx = True
    context.longPolo = False


def longPolo(context):
    order_target_percent(context.poloniex_trading_pair, 0.5)
    order_target_percent(context.bitfinex_trading_pair, -0.5)
    context.longBfx = False
    context.longPolo = True


def analyze(context, perf):
    import matplotlib.pyplot as plt
    perf.loc[:, ['portfolio_value']].plot()
    plt.show()


run_algorithm(initialize=initialize,
              handle_data=handle_data,
              analyze=analyze,
              capital_base=10000,
              live=False,
              base_currency='usd',
              exchange_name='bitfinex, poloniex',
              algo_namespace='Arbitrage',
              data_frequency='minute',
              start=pd.to_datetime('2018-04-02', utc=True),
              end=pd.to_datetime('2018-04-02', utc=True)
              )
