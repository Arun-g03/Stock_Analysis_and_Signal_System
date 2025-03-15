from App.Data_handler import DataHandler
from App.Validator import Validator
from App.Feature_engineering import FeatureEngineering
from App.model import Model
from App.Signal_Generator import SignalGenerator
from App.Screener import StockScreener
from App.Forecasting import ForecastingFactory
from App.Riskmanager import RiskManager
from App.ReportGenerator import ReportGenerator
from App.Visualiser import Visualiser
from App.Logger import System_Log

def main():
    # Configuration
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    
    # Initialize components
    data_handler = DataHandler()
    validator = Validator()
    feature_engineer = FeatureEngineering()
    model_handler = Model()
    signal_generator = SignalGenerator()
    visualiser = Visualiser()
    risk_manager = RiskManager(risk_per_trade=0.02, max_drawdown=0.1)
    screener = StockScreener(min_market_cap=1e10, min_volume=1e6, min_volatility=0.02)
    report_generator = ReportGenerator()
    
    # Data Loading and Validation
    data = data_handler.load_from_yfinance(ticker, start_date, end_date)
    validator.validate_data_integrity(data)
    validator.validate_data_quality(data)
    
    # Feature Engineering
    engineered_data = feature_engineer.engineer_features(data.copy())
    
    # Model Training and Prediction
    model, train_accuracy = model_handler.train_model(engineered_data)
    engineered_data = model_handler.apply_model(engineered_data, model)
    
    # Signal Generation & Backtesting
    engineered_data = signal_generator.generate_rule_based_signals(engineered_data)
    engineered_data = signal_generator.generate_consensus_signal(engineered_data)
    backtested_data = signal_generator.backtest(engineered_data)
    rule_acc, model_acc = signal_generator.evaluate_signals(backtested_data)
    
    # Visualisation
    visualiser.plot_signals(backtested_data, ticker)
    visualiser.plot_balance(backtested_data, ticker)
    
    # Forecasting
    forecaster = ForecastingFactory.get_forecaster("ARIMA", order=(5, 1, 0))
    forecast = forecaster.forecast(data, steps=10)
    
    # Risk Management
    trade_data = {
        'ticker': ticker,
        'entry_price': backtested_data['Close'].iloc[-1],
        'strategy': 'percentage',
        'capital': 10000,
        'atr': engineered_data['ATR'].iloc[-1] if 'ATR' in engineered_data.columns else 1.5,
        'liquidity_data': {'volume': data['Volume'].iloc[-1], 'spread': 0.01}
    }
    risk_assessment = risk_manager.run(trade_data, portfolio_value=backtested_data['Balance'].iloc[-1])
    
    # Stock Screening
    screening_results = screener.run(data)
    
    # Report Generation
    trade_report = backtested_data.to_dict(orient='records')[:10]
    risk_report = [risk_assessment]
    forecast_report = forecast.tolist() if hasattr(forecast, 'tolist') else list(forecast)
    report_file = report_generator.generate_report(trade_report, risk_report, forecast_report)

if __name__ == '__main__':
    main()