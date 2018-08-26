import markets.BfxTrade as bfx
import markets.PoloTrade as polo
import datetime
import time

exchanges = [polo, bfx]
count = 0


def dif(bid, ask):
    return bid / 100 * ask


def compare(dt, bfx, polo):
    bfxBid = bfx['ETHBTC']['bids']['price']
    bfxAsk = bfx['ETHBTC']['asks']['price']

    poloBid = polo['ETHBTC']['bids']['price']
    poloAsk = polo['ETHBTC']['asks']['price']

    if (bfxBid > poloAsk) and (dif(bfxBid, poloAsk) > 0.5):
        print(dt, 'BFX Bid > POLO ASK')
        print(bfxBid, poloAsk)
        f = open('trades.txt', 'a+')
        f.write(dt + '\n')
        f.write('Buy Bitfinex <-> Sell Poloniex' + '\n')
        f.write(bfxBid + ' <-> ' + poloAsk + '\n')
        f.write('Profit: ' + dif(bfxBid, poloAsk) + '\n')
        f.close()

    elif poloBid > bfxAsk and (dif(poloBid, bfxAsk) > 0.5):
        print(dt,'POLO Bid > BFX ASK')
        print(poloBid, bfxAsk)
        f = open('trades.txt', 'a+')
        f.write(dt + '\n')
        f.write('Buy Poloniex <-> Sell Bitfinex' + '\n')
        f.write(poloBid + ' <-> ' + bfxAsk + '\n')
        f.write('Profit: ' + dif(bfxBid, poloAsk) + '\n')
        f.close()

    else:
        print(dt, 'no opportunity found', count)


while True:
    count += 1
    bfxOB = bfx.startExchange()
    poloOB = polo.startExchange()
    dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    compare(dt, bfxOB, poloOB)


