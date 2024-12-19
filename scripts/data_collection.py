import ccxt 
from concurrent.futures import ThreadPoolExecutor


supported_exchanges = [
    "bitbns", "ace", "binanceus", "bequant", "bitopro", "bingx", "bitso",
    "bitcoincom", "bitstamp", "bitget", "bigone", "blockchaincom", "bitmart",
    "bitfinex", "bitpanda", "btcmarkets", "btcalpha", "bitteam", "ascendex",
    "coinbaseexchange", "bitmex", "btcturk", "coinmate", "coinlist",
    "cryptocom", "coinsph", "coinex", "coinmetro", "coinbaseadvanced",
    "coincatch", "coinbase", "exmo", "deribit", "fmfwio", "currencycom",
    "gemini", "delta", "hitbtc", "bitrue", "digifinex", "hollaex", "cex",
    "huobi", "kraken", "htx", "lbank", "indodax", "kuna", "oceanex",
    "novadax", "luno", "ndax", "latoken", "gateio", "p2b", "kucoin",
    "onetrading", "tradeogre", "gate", "mexc", "okx", "phemex", "poloniex",
    "upbit", "probit", "timex", "whitebit", "zonda", "yobit",
    "bitfinex1", "wazirx", "xt"
]

pair = 'BTC/USDT'

market_data = {}

def fetch_market_data(exchange_name):
    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()

        ticker = exchange.fetch_ticker(pair)

        return {
            "exchange": exchange_name,
            "bid": ticker["bid"],
            "ask": ticker["ask"],
            "timestamp": ticker["timestamp"],
        }
    except Exception as e:
        # print(f"Failed to fetch data for {exchange_name}: {e}")
        return None
    
with ThreadPoolExecutor() as executor:
    results = executor.map(fetch_market_data, supported_exchanges)

for result in results:
    if result:
        market_data[result["exchange"]] = result


## solely for debugging purposes, just lists out all the market data on various exchanges
# print("\nCollected Market Data:")
# for exchange, data in market_data.items():
#     print(f"{exchange}: Bid = {data['bid']}, Ask = {data['ask']}, Timestamp = {data['timestamp']}")
    
    

