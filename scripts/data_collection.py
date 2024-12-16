import ccxt 
from concurrent.futures import ThreadPoolExecutor

pair = 'BTC/USD' #declare the pair we want to arbitrage

exchanges = ccxt.exchanges

supported_exchanges = {} #dictionary that supports the exchanges that work for BTC/USD 

##figure out how to make this loop faster.. using "concurrent.futures (threading) may help with this???"
for exc_name in exchanges:
    try:
        exchange_class = getattr(ccxt, exc_name)
        exchange = exchange_class()

        markets = exchange.load_markets()
        if pair in markets:
            supported_exchanges[exchange.id] = exchange
            print(f"{target_pair} is supported on {exchange.id}") #solely for debugging purposes atm 
        else:
            print(f"{target_pair} is not supported on {exchange.id}") #solely for debugging purposes atm


    except Exception as e:  
        print(f"Failed to fetch for {exc_name}: {e}") 

print("\nExchanges supporting the target pair:")
for exchange_id in supported_exchanges:
    print(f"- {exchange_id}")







