# visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def plot_historical_data(data, ticker):
        """
        Plot historical stock price data.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.title(f'Historical Stock Price Data for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    @staticmethod
    def plot_indicator(data, indicator, ticker):
        """
        Plot a specific indicator along with the historical data.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data[indicator], label=indicator)
        plt.title(f'{indicator} for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

    @staticmethod
    def plot_signals(data, ticker):
        """
        Plot buy/sell signals on the historical stock price data.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        buy_signals = data[data['Consensus_Signal'] == 1]
        sell_signals = data[data['Consensus_Signal'] == -1]
        plt.scatter(buy_signals['Date'], buy_signals['Close'], label='Buy Signal', marker='^', color='g')
        plt.scatter(sell_signals['Date'], sell_signals['Close'], label='Sell Signal', marker='v', color='r')
        plt.title(f'Buy/Sell Signals for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    @staticmethod
    def plot_balance(data, ticker):
        """
        Plot balance over time from backtesting.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(data['Date'], data['Balance'], label='Balance')
        plt.title(f'Backtesting Balance for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Balance')
        plt.legend()
        plt.show()

    @staticmethod
    def plot_multiple_indicators(data, indicators, ticker):
        """
        Plot multiple indicators along with the historical data.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        for indicator in indicators:
            plt.plot(data['Date'], data[indicator], label=indicator)
        plt.title(f'Multiple Indicators for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

# Example usage:
# data = pd.read_csv('path_to_your_csv')
# Visualizer.plot_historical_data(data, 'AAPL')
# Visualizer.plot_indicator(data, 'RSI', 'AAPL')
# Visualizer.plot_signals(data, 'AAPL')
# Visualizer.plot_balance(data, 'AAPL')
# Visualizer.plot_multiple_indicators(data, ['RSI', 'MACD', 'BB_High', 'BB_Low'], 'AAPL')
