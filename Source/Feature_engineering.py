# feature_engineering.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from src.patterns import Patterns
from src.indicators import Indicators

class FeatureEngineering:
    @staticmethod
    def add_patterns(data):
        """
        Add patterns as features to the data.
        """
        data = Patterns.higher_highs_lower_lows(data)
        data = Patterns.double_top(data)
        data = Patterns.head_and_shoulders(data)
        data = Patterns.triple_bottom(data)
        data = Patterns.cup_and_handle(data)
        data = Patterns.bullish_engulfing(data)
        data = Patterns.bearish_engulfing(data)
        data = Patterns.morning_star(data)
        data = Patterns.evening_star(data)
        data = Patterns.hammer(data)
        data = Patterns.shooting_star(data)
        data = Patterns.rsi_divergence(data)
        data = Patterns.bollinger_band_squeeze(data)
        data = Patterns.moving_average_crossover(data)
        data = Patterns.adx_trend_strength(data)
        data = Patterns.stochastic_oscillator(data)
        data = Patterns.pennant(data)
        data = Patterns.flag(data)
        data = Patterns.wedge(data)
        data = Patterns.triangle(data)
        return data

    @staticmethod
    def add_indicators(data):
        """
        Add indicators as features to the data.
        """
        data = Indicators.moving_average(data)
        data = Indicators.exponential_moving_average(data)
        data = Indicators.relative_strength_index(data)
        data = Indicators.bollinger_bands(data)
        data = Indicators.macd(data)
        data = Indicators.average_true_range(data)
        data = Indicators.stochastic_oscillator(data)
        data = Indicators.commodity_channel_index(data)
        data = Indicators.ichimoku_cloud(data)
        data = Indicators.aroon(data)
        data = Indicators.parabolic_sar(data)
        data = Indicators.volume_weighted_average_price(data)
        data = Indicators.on_balance_volume(data)
        data = Indicators.money_flow_index(data)
        data = Indicators.chaikin_money_flow(data)
        data = Indicators.ease_of_movement(data)
        data = Indicators.accumulation_distribution(data)
        data = Indicators.ultility_oscillator(data)
        return data

    @staticmethod
    def handle_missing_values(data):
        """
        Handle missing values in the data.
        """
        data.fillna(method='ffill', inplace=True)
        data.fillna(method='bfill', inplace=True)
        return data

    @staticmethod
    def normalize_data(data, columns):
        """
        Normalize specified columns in the data.
        """
        scaler = MinMaxScaler()
        data[columns] = scaler.fit_transform(data[columns])
        return data

    @staticmethod
    def create_lagged_features(data, columns, lags=1):
        """
        Create lagged features for the specified columns.
        """
        for column in columns:
            for lag in range(1, lags + 1):
                data[f'{column}_lag{lag}'] = data[column].shift(lag)
        return data

    @staticmethod
    def engineer_features(data):
        """
        Perform complete feature engineering on the data.
        """
        data = FeatureEngineering.add_patterns(data)
        data = FeatureEngineering.add_indicators(data)
        data = FeatureEngineering.handle_missing_values(data)

        feature_columns = [col for col in data.columns if col not in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        data = FeatureEngineering.create_lagged_features(data, feature_columns, lags=3)
        data = FeatureEngineering.normalize_data(data, feature_columns)

        # Drop rows with NaN values created by lagging
        data.dropna(inplace=True)

        return data

# Example usage:
# data = pd.read_csv('path_to_your_csv')
# data = FeatureEngineering.engineer_features(data)
# print(data.head())
