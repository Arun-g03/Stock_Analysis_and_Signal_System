# signal_generator.py

import pandas as pd
import numpy as np
from src.feature_engineering import FeatureEngineering
from src.model import Model
from sklearn.metrics import accuracy_score

class SignalGenerator:
    @staticmethod
    def generate_rule_based_signals(data):
        """
        Generate trading signals based on patterns and indicators.
        """
        data['Rule_Signal'] = 0

        # Example: Buy signal when RSI < 30 and MACD > MACD Signal
        data.loc[(data['RSI'] < 30) & (data['MACD'] > data['MACD_Signal']), 'Rule_Signal'] = 1
        # Example: Sell signal when RSI > 70 and MACD < MACD Signal
        data.loc[(data['RSI'] > 70) & (data['MACD'] < data['MACD_Signal']), 'Rule_Signal'] = -1

        # Add more rule-based signals as needed
        data.loc[data['bullish_engulfing'], 'Rule_Signal'] = 1
        data.loc[data['bearish_engulfing'], 'Rule_Signal'] = -1

        return data

    @staticmethod
    def generate_consensus_signal(data):
        """
        Generate consensus trading signal based on rule-based and model-based signals.
        """
        data['Consensus_Signal'] = data[['Rule_Signal', 'Model_Signal']].mean(axis=1)
        data['Consensus_Signal'] = data['Consensus_Signal'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
        return data

    @staticmethod
    def backtest(data, initial_balance=10000):
        """
        Backtest trading strategy based on generated signals.
        """
        balance = initial_balance
        position = 0  # 1 for long, -1 for short
        balance_history = []

        for index, row in data.iterrows():
            if row['Consensus_Signal'] == 1:  # Buy signal
                if position <= 0:
                    position = 1
                    balance -= row['Close']  # Buy at close price
            elif row['Consensus_Signal'] == -1:  # Sell signal
                if position >= 0:
                    position = -1
                    balance += row['Close']  # Sell at close price

            # Update balance based on position
            if index > 0:
                balance += position * (row['Close'] - data['Close'].iloc[index - 1])

            balance_history.append(balance)

        data['Balance'] = balance_history

        return data

    @staticmethod
    def evaluate_signals(data):
        """
        Evaluate the accuracy of signals.
        """
        rule_accuracy = accuracy_score(data['Rule_Signal'], data['Consensus_Signal'])
        model_accuracy = accuracy_score(data['Model_Signal'], data['Consensus_Signal'])

        print(f"Rule-Based Signal Accuracy: {rule_accuracy:.2f}")
        print(f"Model-Based Signal Accuracy: {model_accuracy:.2f}")

        return rule_accuracy, model_accuracy

# Example usage:
# data = pd.read_csv('path_to_your_csv')
# data = FeatureEngineering.engineer_features(data)
# data = SignalGenerator.generate_rule_based_signals(data)
# model, model_accuracy = Model.train_model(data)
# Model.save_model(model, 'path_to_save_model')
# model = Model.load_model('path_to_save_model')
# data = Model.apply_model(data, model)
# data = SignalGenerator.generate_consensus_signal(data)
# data = SignalGenerator.backtest(data)
# SignalGenerator.evaluate_signals(data)
# print(data.head())
