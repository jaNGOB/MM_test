# MM_test

It scans two exchanges with the help of CCXT and sees if it can find arbitrage-opportunities between them.

# Example
Balances Exchange A = BTC: 0.1 and USD: 600 \
Balances Exchange B = BTC: 0.1 and USD: 600 

It compares the best bid and ask from both the exchanges and if it sees a high difference it trades. 

Bid Exchange A = 6000 \
Ask Exchange B = 5900

Meaning we could profit 1.7 % if we bought at Exchange B and sold at Exchange A. So we're going to do exactly that. 
Now our Balances look like this:

Balances Exchange A = BTC: 0.0    and USD: 1'200 \
Balances Exchange B = BTC: 0.2017 and USD: 0

Now we have to wait for a reverse opportunity to exchange it back or just split our orders into smaller pieces to profit off of future trades.

# To-Do
Right now there is only the scanning part in place, meaning no orders or order-management happening. 
So if you run it, it will generate a .txt file with the opportunities found.
