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
    def exponential_moving_average(data, window=20):
        """
        Calculate Exponential Moving Average (EMA).
        """
        data[f'EMA_{window}'] = ta.trend.EMAIndicator(data['Close'], window=window).ema_indicator()
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
        data['BB_Mid'] = bb.bollinger_mavg()
        return data

    @staticmethod
    def macd(data, window_slow=26, window_fast=12, window_sign=9):
        """
        Calculate Moving Average Convergence Divergence (MACD).
        """
        macd = ta.trend.MACD(data['Close'], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign)
        data['MACD'] = macd.macd()
        data['MACD_Signal'] = macd.macd_signal()
        data['MACD_Hist'] = macd.macd_diff()
        return data

    @staticmethod
    def average_true_range(data, window=14):
        """
        Calculate Average True Range (ATR).
        """
        data['ATR'] = ta.volatility.AverageTrueRange(data['High'], data['Low'], data['Close'], window=window).average_true_range()
        return data

    @staticmethod
    def stochastic_oscillator(data, window=14, smooth_window=3):
        """
        Calculate Stochastic Oscillator.
        """
        stoch = ta.momentum.StochasticOscillator(data['High'], data['Low'], data['Close'], window=window, smooth_window=smooth_window)
        data['Stoch_K'] = stoch.stoch()
        data['Stoch_D'] = stoch.stoch_signal()
        return data

    @staticmethod
    def commodity_channel_index(data, window=20):
        """
        Calculate Commodity Channel Index (CCI).
        """
        data['CCI'] = ta.trend.CCIIndicator(data['High'], data['Low'], data['Close'], window=window).cci()
        return data

    @staticmethod
    def ichimoku_cloud(data, window1=9, window2=26, window3=52):
        """
        Calculate Ichimoku Cloud components.
        """
        ichimoku = ta.trend.IchimokuIndicator(data['High'], data['Low'], window1=window1, window2=window2, window3=window3)
        data['Ichimoku_Conversion'] = ichimoku.ichimoku_conversion_line()
        data['Ichimoku_Base'] = ichimoku.ichimoku_base_line()
        data['Ichimoku_LeadingA'] = ichimoku.ichimoku_a()
        data['Ichimoku_LeadingB'] = ichimoku.ichimoku_b()
        return data

    @staticmethod
    def aroon(data, window=25):
        """
        Calculate Aroon Indicator.
        """
        aroon = ta.trend.AroonIndicator(data['Close'], window=window)
        data['Aroon_Up'] = aroon.aroon_up()
        data['Aroon_Down'] = aroon.aroon_down()
        return data

    @staticmethod
    def parabolic_sar(data, acceleration=0.02, maximum=0.2):
        """
        Calculate Parabolic SAR.
        """
        data['Parabolic_SAR'] = ta.trend.PSARIndicator(data['High'], data['Low'], data['Close'], step=acceleration, max_step=maximum).psar()
        return data

    @staticmethod
    def volume_weighted_average_price(data, window=14):
        """
        Calculate Volume Weighted Average Price (VWAP).
        """
        vwap = ta.volume.VolumeWeightedAveragePrice(data['High'], data['Low'], data['Close'], data['Volume'], window=window)
        data['VWAP'] = vwap.volume_weighted_average_price()
        return data

    @staticmethod
    def on_balance_volume(data):
        """
        Calculate On-Balance Volume (OBV).
        """
        data['OBV'] = ta.volume.OnBalanceVolumeIndicator(data['Close'], data['Volume']).on_balance_volume()
        return data

    @staticmethod
    def money_flow_index(data, window=14):
        """
        Calculate Money Flow Index (MFI).
        """
        data['MFI'] = ta.volume.MFIIndicator(data['High'], data['Low'], data['Close'], data['Volume'], window=window).money_flow_index()
        return data

    @staticmethod
    def chaikin_money_flow(data, window=20):
        """
        Calculate Chaikin Money Flow (CMF).
        """
        data['CMF'] = ta.volume.ChaikinMoneyFlowIndicator(data['High'], data['Low'], data['Close'], data['Volume'], window=window).chaikin_money_flow()
        return data

    @staticmethod
    def ease_of_movement(data, window=14):
        """
        Calculate Ease of Movement (EOM).
        """
        data['EOM'] = ta.volume.EaseOfMovementIndicator(data['High'], data['Low'], data['Volume'], window=window).ease_of_movement()
        return data

    @staticmethod
    def accumulation_distribution(data):
        """
        Calculate Accumulation/Distribution Index (ADI).
        """
        data['ADI'] = ta.volume.AccDistIndexIndicator(data['High'], data['Low'], data['Close'], data['Volume']).acc_dist_index()
        return data

    @staticmethod
    def ultility_oscillator(data, short_window=7, long_window=14):
        """
        Calculate Utility Oscillator.
        """
        uo = ta.momentum.UltimateOscillator(data['High'], data['Low'], data['Close'], window1=short_window, window2=long_window, window3=28)
        data['Ultimate_Oscillator'] = uo.ultimate_oscillator()
        return data

# Example usage:
# data = pd.read_csv('path_to_your_csv')
# data = Indicators.moving_average(data)
# data = Indicators.exponential_moving_average(data)
# data = Indicators.relative_strength_index(data)
# data = Indicators.bollinger_bands(data)
# data = Indicators.macd(data)
# data = Indicators.average_true_range(data)
# data = Indicators.stochastic_oscillator(data)
# data = Indicators.commodity_channel_index(data)
# data = Indicators.ichimoku_cloud(data)
# data = Indicators.aroon(data)
# data = Indicators.parabolic_sar(data)
# data = Indicators.volume_weighted_average_price(data)
# data = Indicators.on_balance_volume(data)
# data = Indicators.money_flow_index(data)
# data = Indicators.chaikin_money_flow(data)
# data = Indicators.ease_of_movement(data)
# data = Indicators.accumulation_distribution(data)
# data = Indicators.ultility_oscillator(data)
