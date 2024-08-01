# feature_engineering.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from Patterns import Patterns
from Indicators import Indicators
from Logger import System_Log

# Setup the logger
system_logger = System_Log.setup_logger('feature_engineering')

class FeatureEngineering:
    @staticmethod
    def add_patterns(data):
        """
        Add patterns as features to the data.
        """
        try:
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
            system_logger.info("Patterns added successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error adding patterns: {e}")
            raise

    @staticmethod
    def add_indicators(data):
        """
        Add indicators as features to the data.
        """
        try:
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
            data = Indicators.ultimate_oscillator(data)
            system_logger.info("Indicators added successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error adding indicators: {e}")
            raise

    @staticmethod
    def handle_missing_values(data):
        """
        Handle missing values in the data.
        """
        try:
            data.fillna(method='ffill', inplace=True)
            data.fillna(method='bfill', inplace=True)
            system_logger.info("Missing values handled successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error handling missing values: {e}")
            raise

    @staticmethod
    def normalize_data(data, columns):
        """
        Normalize specified columns in the data.
        """
        try:
            scaler = MinMaxScaler()
            data[columns] = scaler.fit_transform(data[columns])
            system_logger.info("Data normalized successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error normalizing data: {e}")
            raise

    @staticmethod
    def create_lagged_features(data, columns, lags=1):
        """
        Create lagged features for the specified columns.
        """
        try:
            for column in columns:
                for lag in range(1, lags + 1):
                    data[f'{column}_lag{lag}'] = data[column].shift(lag)
            system_logger.info("Lagged features created successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error creating lagged features: {e}")
            raise

    @staticmethod
    def engineer_features(data):
        """
        Perform complete feature engineering on the data.
        """
        try:
            data = FeatureEngineering.add_patterns(data)
            data = FeatureEngineering.add_indicators(data)
            data = FeatureEngineering.handle_missing_values(data)

            feature_columns = [col for col in data.columns if col not in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
            data = FeatureEngineering.create_lagged_features(data, feature_columns, lags=3)
            data = FeatureEngineering.normalize_data(data, feature_columns)

            # Drop rows with NaN values created by lagging
            data.dropna(inplace=True)

            system_logger.info("Feature engineering completed successfully.")
            return data
        except Exception as e:
            system_logger.error(f"Error in feature engineering: {e}")
            raise

# Example usage:
# data = pd.read_csv('path_to_your_csv')
# data = FeatureEngineering.engineer_features(data)
# print(data.head())
