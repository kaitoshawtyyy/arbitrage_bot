import ccxt 
from concurrent.futures import ThreadPoolExecutor

pair = 'BTC/USDT' #declare the pair we want to arbitrage
exchanges = ccxt.exchanges

def check_btcusdt(exchange_name):
    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()

        markets = exchange.load_markets()

        if pair in markets:
            supported_exchanges[exchange.id] = exchange
            print(f"{pair} is supported on {exchange.id}") #solely for debugging purposes atm 
        else:
            print(f"{pair} is not supported on {exchange.id}") #solely for debugging purposes atm


    except Exception as e:  
        print(f"Failed to fetch for {exchange_name}: {e}") 
    return None

with ThreadPoolExecutor() as executor:
    results = executor.map(check_btcusdt, exchanges)

# Collect results
for result in results:
    if result:
        exchange_id, market_data = result
        supported_exchanges[exchange_id] = market_data


print("\nExchanges supporting the target pair:")
for exchange_id in supported_exchanges:
    print(f"- {exchange_id}")


