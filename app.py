import MM.markets.BfxTrade as bfx
import MM.markets.PoloTrade as polo
import time

exchanges = [polo, bfx]
count = 0


def dif(bid, ask):
    return bid / 100 * ask


def compare(bfx, polo):
    bfxBid = bfx['ETHBTC']['bids']['price']
    bfxAsk = bfx['ETHBTC']['asks']['price']

    poloBid = polo['ETHBTC']['bids']['price']
    poloAsk = polo['ETHBTC']['asks']['price']

    if (bfxBid > poloAsk) and (dif(bfxBid, poloAsk) > 0.5):
        print('BFX Bid > POLO ASK')
        print(bfxBid, poloAsk)
    elif poloBid > bfxAsk and (dif(poloBid, bfxAsk) > 0.5):
        print('POLO Bid > BFX ASK')
        print(poloBid, bfxAsk)
    else:
        print('no opportunity found', count)


while True:
    count += 1
    bfxOB = bfx.startExchange()
    poloOB = polo.startExchange()

    compare(bfxOB, poloOB)
