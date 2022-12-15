import pandas as pd 
import yfinance as yf
from datetime import date

def daily_data() : 
    #Getting Ticker symbols from https://www.nasdaq.com/market-activity/quotes/nasdaq-ndx-index
    nasdaq_df = pd.read_csv("Stocks in the NASDAQ-100 Index.csv") #Creating a pandas df with table from html source
    nasdaq_symbols = nasdaq_df["Symbol"] #Using only the symbols columns
    nasdaq_symbols = list(nasdaq_symbols.values) #Converting symbols to a list

    #Using yfinance to get data from the tickers
    data = yf.download(tickers=nasdaq_symbols)
    today = date.today()
    data.to_csv(f"results/nasdaq_{today}.csv")
    


daily_data()
