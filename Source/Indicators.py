# indicators.py

import pandas as pd
import ta
from Logger import System_Log

# Setup the logger
system_logger = System_Log.setup_logger('indicators')

class Indicators:
    @staticmethod
    def moving_average(data, window=20):
        """
        Calculate Moving Average.
        """
        try:
            data[f'MA_{window}'] = ta.trend.SMAIndicator(data['Close'], window=window).sma_indicator()
            system_logger.info(f"Moving Average (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Moving Average: {e}")
            raise

    @staticmethod
    def exponential_moving_average(data, window=20):
        """
        Calculate Exponential Moving Average (EMA).
        """
        try:
            data[f'EMA_{window}'] = ta.trend.EMAIndicator(data['Close'], window=window).ema_indicator()
            system_logger.info(f"Exponential Moving Average (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Exponential Moving Average: {e}")
            raise

    @staticmethod
    def relative_strength_index(data, window=14):
        """
        Calculate Relative Strength Index (RSI).
        """
        try:
            data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=window).rsi()
            system_logger.info(f"Relative Strength Index (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Relative Strength Index: {e}")
            raise

    @staticmethod
    def bollinger_bands(data, window=20, std_dev=2):
        """
        Calculate Bollinger Bands.
        """
        try:
            bb = ta.volatility.BollingerBands(data['Close'], window=window, window_dev=std_dev)
            data['BB_High'] = bb.bollinger_hband()
            data['BB_Low'] = bb.bollinger_lband()
            data['BB_Mid'] = bb.bollinger_mavg()
            system_logger.info(f"Bollinger Bands (window={window}, std_dev={std_dev}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Bollinger Bands: {e}")
            raise

    @staticmethod
    def macd(data, window_slow=26, window_fast=12, window_sign=9):
        """
        Calculate Moving Average Convergence Divergence (MACD).
        """
        try:
            macd = ta.trend.MACD(data['Close'], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign)
            data['MACD'] = macd.macd()
            data['MACD_Signal'] = macd.macd_signal()
            data['MACD_Hist'] = macd.macd_diff()
            system_logger.info(f"MACD (slow={window_slow}, fast={window_fast}, sign={window_sign}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating MACD: {e}")
            raise

    @staticmethod
    def average_true_range(data, window=14):
        """
        Calculate Average True Range (ATR).
        """
        try:
            data['ATR'] = ta.volatility.AverageTrueRange(data['High'], data['Low'], data['Close'], window=window).average_true_range()
            system_logger.info(f"Average True Range (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Average True Range: {e}")
            raise

    @staticmethod
    def stochastic_oscillator(data, window=14, smooth_window=3):
        """
        Calculate Stochastic Oscillator.
        """
        try:
            stoch = ta.momentum.StochasticOscillator(data['High'], data['Low'], data['Close'], window=window, smooth_window=smooth_window)
            data['Stoch_K'] = stoch.stoch()
            data['Stoch_D'] = stoch.stoch_signal()
            system_logger.info(f"Stochastic Oscillator (window={window}, smooth_window={smooth_window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Stochastic Oscillator: {e}")
            raise

    @staticmethod
    def commodity_channel_index(data, window=20):
        """
        Calculate Commodity Channel Index (CCI).
        """
        try:
            data['CCI'] = ta.trend.CCIIndicator(data['High'], data['Low'], data['Close'], window=window).cci()
            system_logger.info(f"Commodity Channel Index (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Commodity Channel Index: {e}")
            raise

    @staticmethod
    def ichimoku_cloud(data, window1=9, window2=26, window3=52):
        """
        Calculate Ichimoku Cloud components.
        """
        try:
            ichimoku = ta.trend.IchimokuIndicator(data['High'], data['Low'], window1=window1, window2=window2, window3=window3)
            data['Ichimoku_Conversion'] = ichimoku.ichimoku_conversion_line()
            data['Ichimoku_Base'] = ichimoku.ichimoku_base_line()
            data['Ichimoku_LeadingA'] = ichimoku.ichimoku_a()
            data['Ichimoku_LeadingB'] = ichimoku.ichimoku_b()
            system_logger.info(f"Ichimoku Cloud (window1={window1}, window2={window2}, window3={window3}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Ichimoku Cloud: {e}")
            raise

    @staticmethod
    def aroon(data, window=25):
        """
        Calculate Aroon Indicator.
        """
        try:
            aroon = ta.trend.AroonIndicator(data['Close'], window=window)
            data['Aroon_Up'] = aroon.aroon_up()
            data['Aroon_Down'] = aroon.aroon_down()
            system_logger.info(f"Aroon Indicator (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Aroon Indicator: {e}")
            raise

    @staticmethod
    def parabolic_sar(data, acceleration=0.02, maximum=0.2):
        """
        Calculate Parabolic SAR.
        """
        try:
            data['Parabolic_SAR'] = ta.trend.PSARIndicator(data['High'], data['Low'], data['Close'], step=acceleration, max_step=maximum).psar()
            system_logger.info(f"Parabolic SAR (acceleration={acceleration}, maximum={maximum}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Parabolic SAR: {e}")
            raise

    @staticmethod
    def volume_weighted_average_price(data, window=14):
        """
        Calculate Volume Weighted Average Price (VWAP).
        """
        try:
            vwap = ta.volume.VolumeWeightedAveragePrice(data['High'], data['Low'], data['Close'], data['Volume'], window=window)
            data['VWAP'] = vwap.volume_weighted_average_price()
            system_logger.info(f"Volume Weighted Average Price (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating VWAP: {e}")
            raise

    @staticmethod
    def on_balance_volume(data):
        """
        Calculate On-Balance Volume (OBV).
        """
        try:
            data['OBV'] = ta.volume.OnBalanceVolumeIndicator(data['Close'], data['Volume']).on_balance_volume()
            system_logger.info(f"On-Balance Volume calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating OBV: {e}")
            raise

    @staticmethod
    def money_flow_index(data, window=14):
        """
        Calculate Money Flow Index (MFI).
        """
        try:
            data['MFI'] = ta.volume.MFIIndicator(data['High'], data['Low'], data['Close'], data['Volume'], window=window).money_flow_index()
            system_logger.info(f"Money Flow Index (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating MFI: {e}")
            raise

    @staticmethod
    def chaikin_money_flow(data, window=20):
        """
        Calculate Chaikin Money Flow (CMF).
        """
        try:
            data['CMF'] = ta.volume.ChaikinMoneyFlowIndicator(data['High'], data['Low'], data['Close'], data['Volume'], window=window).chaikin_money_flow()
            system_logger.info(f"Chaikin Money Flow (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating CMF: {e}")
            raise

    @staticmethod
    def ease_of_movement(data, window=14):
        """
        Calculate Ease of Movement (EOM).
        """
        try:
            data['EOM'] = ta.volume.EaseOfMovementIndicator(data['High'], data['Low'], data['Volume'], window=window).ease_of_movement()
            system_logger.info(f"Ease of Movement (window={window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating EOM: {e}")
            raise

    @staticmethod
    def accumulation_distribution(data):
        """
        Calculate Accumulation/Distribution Index (ADI).
        """
        try:
            data['ADI'] = ta.volume.AccDistIndexIndicator(data['High'], data['Low'], data['Close'], data['Volume']).acc_dist_index()
            system_logger.info(f"Accumulation/Distribution Index calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating ADI: {e}")
            raise

    @staticmethod
    def ultimate_oscillator(data, short_window=7, long_window=14):
        """
        Calculate Ultimate Oscillator.
        """
        try:
            uo = ta.momentum.UltimateOscillator(data['High'], data['Low'], data['Close'], window1=short_window, window2=long_window, window3=28)
            data['Ultimate_Oscillator'] = uo.ultimate_oscillator()
            system_logger.info(f"Ultimate Oscillator (short_window={short_window}, long_window={long_window}) calculated successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error calculating Ultimate Oscillator: {e}")
            raise

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
# data = Indicators.ultimate_oscillator(data)
