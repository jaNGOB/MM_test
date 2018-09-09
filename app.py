import markets.BfxTrade as bfx
import markets.PoloTrade as polo
from utils import compare, dif
import datetime
import time

count = 0
exchanges = [polo, bfx]

while True:
    count += 1
    bfxOB = bfx.startExchange()
    poloOB = polo.startExchange()
    dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    compare(dt, count, bfxOB, poloOB)
