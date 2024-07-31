# data_handler.py

import pandas as pd
import yfinance as yf
import alpaca_trade_api as tradeapi

class DataHandler:
    @staticmethod
    def load_from_csv(file_path):
        """
        Load historical data from a CSV file.
        """
        data = pd.read_csv(file_path, parse_dates=['Date'])
        return data

    @staticmethod
    def load_from_yfinance(ticker, start_date, end_date):
        """
        Load historical data from Yahoo Finance.
        """
        data = yf.download(ticker, start=start_date, end=end_date)
        data.reset_index(inplace=True)
        return data

    @staticmethod
    def load_from_alpaca(ticker, start_date, end_date, api_key, api_secret, base_url):
        """
        Load historical data from Alpaca API.
        """
        api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
        barset = api.get_barset(ticker, 'day', start=start_date, end=end_date)
        bars = barset[ticker]
        
        data = pd.DataFrame({
            'Date': [bar.t for bar in bars],
            'Open': [bar.o for bar in bars],
            'High': [bar.h for bar in bars],
            'Low': [bar.l for bar in bars],
            'Close': [bar.c for bar in bars],
            'Volume': [bar.v for bar in bars]
            
        })
        
        return data

# Example usage:
# data_csv = DataHandler.load_from_csv('path_to_your_csv.csv')
# data_yf = DataHandler.load_from_yfinance('AAPL', '2020-01-01', '2021-01-01')
# data_alpaca = DataHandler.load_from_alpaca('AAPL', '2020-01-01', '2021-01-01', 'your_api_key', 'your_api_secret', 'https://paper-api.alpaca.markets')
