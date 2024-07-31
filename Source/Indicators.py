# indicators.py

import pandas as pd
import ta

class Indicators:
    @staticmethod
    def moving_average(data, window=20):
        """
        Calculate Moving Average.
        """
        data[f'MA_{window}'] = ta.trend.SMAIndicator(data['Close'], window=window).sma_indicator()
        return data

    @staticmethod
    def relative_strength_index(data, window=14):
        """
        Calculate Relative Strength Index (RSI).
        """
        data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=window).rsi()
        return data

    @staticmethod
    def bollinger_bands(data, window=20, std_dev=2):
        """
        Calculate Bollinger Bands.
        """
        bb = ta.volatility.BollingerBands(data['Close'], window=window, window_dev=std_dev)
        data['BB_High'] = bb.bollinger_hband()
        data['BB_Low'] = bb.bollinger_lband()
        return data

    @staticmethod
    def macd(data, window_slow=26, window_fast=12, window_sign=9):
        """
        Calculate Moving Average Convergence Divergence (MACD).
        """
        macd = ta.trend.MACD(data['Close'], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign)
        data['MACD'] = macd.macd()
        data['MACD_Signal'] = macd.macd_signal()
        return data

    @staticmethod
    def average_true_range(data, window=14):
        """
        Calculate Average True Range (ATR).
        """
        data['ATR'] = ta.volatility.AverageTrueRange(data['High'], data['Low'], data['Close'], window=window).average_true_range()
        return data

