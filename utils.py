import markets.BfxTrade as bfx
import markets.PoloTrade as polo


def dif(bid, ask):
    return (100 / bid * ask) - 100


def compare(dt, count, bfx, polo):
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
        print(dt, 'POLO Bid > BFX ASK')
        print(poloBid, bfxAsk)
        f = open('trades.txt', 'a+')
        f.write(dt + '\n')
        f.write('Buy Poloniex <-> Sell Bitfinex' + '\n')
        f.write(poloBid + ' <-> ' + bfxAsk + '\n')
        f.write('Profit: ' + dif(bfxBid, poloAsk) + '\n')
        f.close()

    else:
        print(dt, 'no opportunity found', count)
        # print('PoloAsk: {} PoloBid: {}'.format(poloAsk, poloBid))
        # print(dif(poloBid, bfxAsk))
        # print('BfxAsk : {} BfxBid : {}'.format(bfxAsk, bfxBid))
        # print(dif(bfxBid, poloAsk))


def getBalances():
    bfxBal = bfx.getBalance()
    bfxBalETH = bfxBal['ETH']
    bfxBalBTC = bfxBal['BTC']

    poloBal = polo.getBalance()
    poloBalBTC = poloBal['BTC']
    poloBalETH = poloBal['ETH']




