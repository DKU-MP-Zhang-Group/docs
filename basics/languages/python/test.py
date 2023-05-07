# import yfinance as yf
# import pandas as pd

# url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv"
# tickers = pd.read_csv(url)
# sp500_list = tickers['Symbol'].to_list()

# # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# data = yf.download("^GSPC", interval="1d", start="1988-01-01", end="2023-12-31")
# data.to_csv('out.csv')

# def get_y_value(x):
#     y = 5*x**3 + x**2 + x-3
#     return y

# print(get_y_value(10))

import yfinance as yf
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
data = yf.download(tickers="^GSPC", interval="1d", start="1988-01-01", end="2023-12-31")
data.to_csv('./out.csv')