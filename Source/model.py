# model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

class Model:
    @staticmethod
    def train_model(data, target_column='Signal'):
        """
        Train a machine learning model to generate trading signals.
        """
        feature_columns = [col for col in data.columns if col not in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', target_column]]
        X = data[feature_columns]
        y = data[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        return model, accuracy

    @staticmethod
    def save_model(model, file_path):
        """
        Save the trained model to a file.
        """
        joblib.dump(model, file_path)

    @staticmethod
    def load_model(file_path):
        """
        Load a trained model from a file.
        """
        return joblib.load(file_path)

    @staticmethod
    def apply_model(data, model):
        """
        Apply a trained model to generate trading signals.
        """
        feature_columns = [col for col in data.columns if col not in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Signal']]
        X = data[feature_columns]
        data['Model_Signal'] = model.predict(X)

        return data
