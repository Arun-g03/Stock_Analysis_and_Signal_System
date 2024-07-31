import pandas as pd

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