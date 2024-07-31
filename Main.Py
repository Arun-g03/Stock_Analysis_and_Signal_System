# main.py

from src.data_handler import DataHandler
from src.feature_engineering import FeatureEngineering
from src.signal_generator import SignalGenerator
from src.model import Model
from src.visualizer import Visualizer
from src.validator import Validator
from config.config import LOG_PATH

def main():
    try:
        # Load data from CSV
        data = DataHandler.load_from_csv('path_to_your_csv.csv')
        # Validate Data Integrity and Quality
        Validator.validate_data_integrity(data)
        Validator.validate_data_quality(data)

        # Feature Engineering
        data = FeatureEngineering.engineer_features(data)
        # Validate Processed Data
        Validator.validate_processed_data(data)

        # Generate Rule-Based Signals
        data = SignalGenerator.generate_rule_based_signals(data)

        # Train Model
        model, model_accuracy = Model.train_model(data, target_column='Rule_Signal')
        Model.save_model(model, 'model/random_forest_model.pkl')

        # Load Model and Apply Model-Based Signals
        model = Model.load_model('model/random_forest_model.pkl')
        data = Model.apply_model(data, model)

        # Generate Consensus Signals
        data = SignalGenerator.generate_consensus_signal(data)

        # Backtest
        data = SignalGenerator.backtest(data)

        # Evaluate Signals
        SignalGenerator.evaluate_signals(data)

        # Validate Model Results
        Validator.validate_model_results(data)

        # Visualize Results
        ticker = 'AAPL'  # Replace with your ticker if different
        Visualizer.plot_historical_data(data, ticker)
        Visualizer.plot_indicator(data, 'RSI', ticker)
        Visualizer.plot_signals(data, ticker)
        Visualizer.plot_balance(data, ticker)
        Visualizer.plot_multiple_indicators(data, ['RSI', 'MACD', 'BB_High', 'BB_Low'], ticker)

    except Exception as e:
        system_logger = System_Log.setup_logger('main', LOG_PATH)
        system_logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
