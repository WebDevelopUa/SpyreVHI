# Project description
# googlefinance.client is a python client library for google finance api

from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Dow Jones
param = {
    'q': ".DJI",  # Stock symbol (ex: "AAPL")
    'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
    'x': "INDEXDJX",  # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1Y"  # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = get_price_data(param)
print(df)

params = [
    # Dow Jones
    {
        'q': ".DJI",
        'x': "INDEXDJX",
    },
    # NYSE COMPOSITE (DJ)
    {
        'q': "NYA",
        'x': "INDEXNYSEGIS",
    },
    # S&P 500
    {
        'q': ".INX",
        'x': "INDEXSP",
    }
]
period = "1Y"
# get open, high, low, close, volume data (return pandas dataframe)
df = get_prices_data(params, period)
print(df)

params = [
    # Dow Jones
    {
        'q': ".DJI",
        'x': "INDEXDJX",
    },
    # NYSE COMPOSITE (DJ)
    {
        'q': "NYA",
        'x': "INDEXNYSEGIS",
    },
    # S&P 500
    {
        'q': ".INX",
        'x': "INDEXSP",
    }
]
period = "1Y"
interval = 60 * 30  # 30 minutes
# get open, high, low, close, volume time data (return pandas dataframe)
df = get_prices_time_data(params, period, interval)
print(df)
