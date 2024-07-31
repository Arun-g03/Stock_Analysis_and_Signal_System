# patterns.py

import pandas as pd
import numpy as np

class Patterns:
    @staticmethod
    def higher_highs_lower_lows(data, window=20):
        """
        Identify Higher Highs and Lower Lows in the data.
        """
        data['high_max'] = data['High'].rolling(window=window).max()
        data['low_min'] = data['Low'].rolling(window=window).min()
        data['higher_highs'] = data['High'] > data['high_max'].shift(1)
        data['lower_lows'] = data['Low'] < data['low_min'].shift(1)
        return data

    @staticmethod
    def double_top(data, window=20):
        """
        Identify Double Top pattern in the data.
        """
        data['high_max'] = data['High'].rolling(window=window).max()
        data['double_top'] = (data['High'] == data['high_max']) & (data['High'].shift(window) == data['high_max'])
        return data

    @staticmethod
    def head_and_shoulders(data, window=20):
        """
        Identify Head and Shoulders pattern in the data.
        """
        data['head_and_shoulders'] = ((data['High'].shift(2*window) < data['High'].shift(window)) &
                                      (data['High'] > data['High'].shift(window)) &
                                      (data['High'] > data['High'].shift(2*window)) &
                                      (data['High'].shift(window) < data['High'].shift(2*window)) &
                                      (data['High'] < data['High'].shift(2*window)))
        return data

    @staticmethod
    def triple_bottom(data, window=20):
        """
        Identify Triple Bottom pattern in the data.
        """
        data['low_min'] = data['Low'].rolling(window=window).min()
        data['triple_bottom'] = ((data['Low'] == data['low_min']) &
                                 (data['Low'].shift(window) == data['low_min']) &
                                 (data['Low'].shift(2*window) == data['low_min']))
        return data

    @staticmethod
    def cup_and_handle(data, window=20):
        """
        Identify Cup and Handle pattern in the data.
        """
        data['cup'] = (data['High'].rolling(window).max() - data['Low'].rolling(window).min())
        data['handle'] = (data['High'].shift(window//2).rolling(window).max() - data['Low'].shift(window//2).rolling(window).min())
        data['cup_and_handle'] = data['handle'] < data['cup']
        return data

    @staticmethod
    def bullish_engulfing(data):
        """
        Identify Bullish Engulfing pattern in the data.
        """
        data['bullish_engulfing'] = ((data['Open'].shift(1) > data['Close'].shift(1)) &
                                     (data['Open'] < data['Close']) &
                                     (data['Open'] < data['Close'].shift(1)) &
                                     (data['Close'] > data['Open'].shift(1)))
        return data

    @staticmethod
    def bearish_engulfing(data):
        """
        Identify Bearish Engulfing pattern in the data.
        """
        data['bearish_engulfing'] = ((data['Open'].shift(1) < data['Close'].shift(1)) &
                                     (data['Open'] > data['Close']) &
                                     (data['Open'] > data['Close'].shift(1)) &
                                     (data['Close'] < data['Open'].shift(1)))
        return data

    @staticmethod
    def morning_star(data):
        """
        Identify Morning Star pattern in the data.
        """
        data['morning_star'] = ((data['Close'].shift(2) < data['Open'].shift(2)) &
                                (data['Close'].shift(1) < data['Open'].shift(1)) &
                                (data['Close'] > data['Open']))
        return data

    @staticmethod
    def evening_star(data):
        """
        Identify Evening Star pattern in the data.
        """
        data['evening_star'] = ((data['Close'].shift(2) > data['Open'].shift(2)) &
                                (data['Close'].shift(1) > data['Open'].shift(1)) &
                                (data['Close'] < data['Open']))
        return data

    @staticmethod
    def hammer(data):
        """
        Identify Hammer pattern in the data.
        """
        body_size = abs(data['Close'] - data['Open'])
        lower_shadow = data['Open'] - data['Low']
        data['hammer'] = (lower_shadow > body_size * 2) & (data['Close'] > data['Open'])
        return data

    @staticmethod
    def shooting_star(data):
        """
        Identify Shooting Star pattern in the data.
        """
        body_size = abs(data['Close'] - data['Open'])
        upper_shadow = data['High'] - data['Close']
        data['shooting_star'] = (upper_shadow > body_size * 2) & (data['Open'] > data['Close'])
        return data

    @staticmethod
    def rsi_divergence(data, window=14):
        """
        Identify RSI Divergence in the data.
        """
        data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=window).rsi()
        data['price_diff'] = data['Close'].diff(window)
        data['rsi_diff'] = data['RSI'].diff(window)
        data['rsi_divergence'] = (data['price_diff'] * data['rsi_diff'] < 0)
        return data

    @staticmethod
    def bollinger_band_squeeze(data, window=20, std_dev=2):
        """
        Identify Bollinger Band Squeeze in the data.
        """
        bb = ta.volatility.BollingerBands(data['Close'], window=window, window_dev=std_dev)
        data['bb_squeeze'] = (bb.bollinger_hband() - bb.bollinger_lband()) / data['Close']
        data['bollinger_band_squeeze'] = data['bb_squeeze'] < (std_dev / 2)
        return data

    @staticmethod
    def moving_average_crossover(data, short_window=50, long_window=200):
        """
        Identify Moving Average Crossover in the data.
        """
        data['short_ma'] = ta.trend.SMAIndicator(data['Close'], window=short_window).sma_indicator()
        data['long_ma'] = ta.trend.SMAIndicator(data['Close'], window=long_window).sma_indicator()
        data['ma_crossover'] = data['short_ma'] > data['long_ma']
        data['ma_crossover_signal'] = data['ma_crossover'] & ~data['ma_crossover'].shift(1)
        return data

    @staticmethod
    def adx_trend_strength(data, window=14):
        """
        Identify ADX Trend Strength in the data.
        """
        adx = ta.trend.ADXIndicator(data['High'], data['Low'], data['Close'], window=window)
        data['adx'] = adx.adx()
        data['strong_trend'] = data['adx'] > 25
        return data

    @staticmethod
    def stochastic_oscillator(data, window=14):
        """
        Identify Stochastic Oscillator in the data.
        """
        stoch = ta.momentum.StochasticOscillator(data['High'], data['Low'], data['Close'], window=window)
        data['stoch_k'] = stoch.stoch()
        data['stoch_d'] = stoch.stoch_signal()
        data['stoch_overbought'] = data['stoch_k'] > 80
        data['stoch_oversold'] = data['stoch_k'] < 20
        return data

    @staticmethod
    def pennant(data, window=20):
        """
        Identify Pennant pattern in the data.
        """
        data['pennant'] = ((data['Close'] > data['Close'].shift(window)) & 
                           (data['Close'] < data['Close'].shift(window * 2)) &
                           (data['High'] < data['High'].shift(window)) &
                           (data['Low'] > data['Low'].shift(window)))
        return data

    @staticmethod
    def flag(data, window=20):
        """
        Identify Flag pattern in the data.
        """
        data['flag'] = ((data['Close'] > data['Close'].shift(window)) &
                        (data['Close'] < data['Close'].shift(window * 2)) &
                        (data['High'] < data['High'].shift(window)) &
                        (data['Low'] > data['Low'].shift(window)) &
                        (data['Volume'] > data['Volume'].shift(window)))
        return data

    @staticmethod
    def wedge(data, window=20):
        """
        Identify Wedge pattern in the data.
        """
        data['wedge'] = ((data['High'].rolling(window).max() - data['Low'].rolling(window).min()) /
                         (data['High'].rolling(window * 2).max() - data['Low'].rolling(window * 2).min()) < 0.5)
        return data

    @staticmethod
    def triangle(data, window=20):
        """
        Identify Triangle pattern in the data.
        """
        data['high_trend'] = data['High'].rolling(window).max()
        data['low_trend'] = data['Low'].rolling(window).min()
        data['triangle'] = (data['High'] < data['high_trend']) & (data['Low'] > data['low_trend'])
        return data
    # Additional patterns can be added here...

# Example usage:
# data = pd.read_csv('path_to_your_csv')
# data = Patterns.higher_highs_lower_lows(data)
# data = Patterns.double_top(data)
# data = Patterns.head_and_shoulders(data)
# data = Patterns.triple_bottom(data)
# data = Patterns.cup_and_handle(data)
# data = Patterns.bullish_engulfing(data)
# data = Patterns.bearish_engulfing(data)
# data = Patterns.morning_star(data)
# data = Patterns.evening_star(data)
# data = Patterns.hammer(data)
# data = Patterns.shooting_star(data)
# data = Patterns.rsi_divergence(data)
# data = Patterns.bollinger_band_squeeze(data)
# data = Patterns.moving_average_crossover(data)
# data = Patterns.adx_trend_strength(data)
# data = Patterns.stochastic_oscillator(data)
# data = Patterns.pennant(data)
# data = Patterns.flag(data)
# data = Patterns.wedge(data)
# data = Patterns.triangle(data)