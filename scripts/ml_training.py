import ccxt
import pandas as pd 
from data_collection import supported_exchanges
from concurrent.futures import ThreadPoolExecutor

bars = []
pair = 'BTC/USDT'
timeframe = '15m'
limit = 500

# figure out how to separate exchanges..
# do we need separate dataframes, or can we just figure out a dividng point in the single dataframe
# after all, we need to compare exchange to exchange... 

def fetchohlcv(exchange_name):

    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()

        exchange.load_markets()

        if exchange.has['fetchOHLCV'] and pair in exchange.markets:
            ohlcv = exchange.fetch_ohlcv(pair, timeframe, limit)
            
            return [ 
            {
                 'exchange': exchange_name,
                'timestamp': bar[0],
                'open': bar[1],
                'high': bar[2],
                'low': bar[3],                    
                'close': bar[4],
                'volume': bar[5],
            }
            for bar in ohlcv
            ]
        else:  
            print(f"Failed to find ohlcv for {exchange_name}: {e}")
            return None
        
    except Exception as e:
        print(f"Failed to fetch data for {exchange_name}: {e}")

with ThreadPoolExecutor() as executor:
    results = executor.map(fetchohlcv, supported_exchanges)

for result in results:
    if result: 
        bars.extend(result)

df = pd.DataFrame(bars)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

print(df)
    
   



