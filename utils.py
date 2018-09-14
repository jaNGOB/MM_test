import markets.BfxTrade as bfx
import markets.PoloTrade as polo


def dif(bid, ask):
    return (100 / ask * bid) - 100


def compare(dt, count, bfx, polo, verbose=False):
    bfxBid = bfx['ETHBTC']['bids']['price']
    bfxAsk = bfx['ETHBTC']['asks']['price']

    poloBid = polo['ETHBTC']['bids']['price']
    poloAsk = polo['ETHBTC']['asks']['price']

    if (bfxBid > poloAsk) and (dif(bfxBid, poloAsk) > 0.5):
        print(dt, 'BFX Bid > POLO ASK')
        print(bfxBid, poloAsk)
        f = open('trades.txt', 'a+')
        f.write(dt + '\n')
        f.write('Buy Bitfinex <-> Sell Poloniex \n')
        f.write('{} <-> {} \n'.format(bfxBid, poloAsk))
        f.write('Profit: {} \n'.format(dif(bfxBid, poloAsk)))
        f.close()

    elif poloBid > bfxAsk and (dif(poloBid, bfxAsk) > 0.5):
        print(dt, 'POLO Bid > BFX ASK')
        print(poloBid, bfxAsk)
        f = open('trades.txt', 'a+')
        f.write(dt + '\n')
        f.write('Buy Poloniex <-> Sell Bitfinex \n')
        f.write('{} <-> {} \n'.format(poloBid, bfxAsk))
        f.write('Profit: {} \n'.format(dif(bfxBid, poloAsk)))
        f.close()

    else:
        print(dt, 'no opportunity found', count)
        # print('PoloBid: {} BfxAsk : {}'.format(poloBid, bfxAsk))
        # print('Dif. not big enough: {}'.format(dif(poloBid, bfxAsk)))
        # print('BfxBid : {} PoloAsk: {}'.format(bfxBid, poloAsk))
        # print('Dif. not big enough: {}'.format(dif(bfxBid, poloAsk)))


def getBalances():
    bfxBal = bfx.getBalance()
    bfxBalETH = bfxBal['ETH']
    bfxBalBTC = bfxBal['BTC']

    poloBal = polo.getBalance()
    poloBalBTC = poloBal['BTC']
    poloBalETH = poloBal['ETH']




