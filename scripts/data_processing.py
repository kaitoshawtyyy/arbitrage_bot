import pandas as pd
import ccxt

from data_collection import market_data # this retrieves market_data from data_collection

df = pd.DataFrame(market_data).T #read in market_data and tranpose

df = df.dropna(subset=['bid', 'ask'])

# Ensure all values in 'bid' and 'ask' are numeric - thsi is probably redundant.. 
# df = df[(pd.to_numeric(df['bid'], errors='coerce').notna()) & 
#         (pd.to_numeric(df['ask'], errors='coerce').notna())]

#df['spread'] = (df['ask'] - df['bid']) / df['ask']

#calculations:
maxbidprice = df.loc[df['bid'].idxmax()]
minaskprice = df.loc[df['ask'].idxmin()]

#df['spread'] = (maxbidprice - df['ask']) /df['ask']

spread = (maxbidprice['bid'] - minaskprice['ask']) / minaskprice['ask']

print(spread)
print(f"buy here {minaskprice['exchange']}")
print(f"sell here {maxbidprice['exchange']}")


















