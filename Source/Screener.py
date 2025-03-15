import pandas as pd

class StockScreener:
    def __init__(self, min_market_cap: float, min_volume: int, min_volatility: float):
        """Initialise screener with fundamental and technical thresholds."""
        self.min_market_cap = min_market_cap
        self.min_volume = min_volume
        self.min_volatility = min_volatility
        self.data = None
    
    # 🔹 Fundamental Screening
    def filter_by_market_cap(self, data: pd.DataFrame, min_cap: float) -> pd.DataFrame:
        """Filter stocks based on market capitalisation."""
        return data[data['market_cap'] >= min_cap]
    
    def filter_by_volume(self, data: pd.DataFrame, min_volume: int) -> pd.DataFrame:
        """Filter out stocks with low trading volume."""
        return data[data['volume'] >= min_volume]
    
    def filter_by_volatility(self, data: pd.DataFrame, min_volatility: float) -> pd.DataFrame:
        """Remove stocks with very low price movement."""
        return data[data['volatility'] >= min_volatility]
    
    # 🔹 Technical Screening (Short-Term)
    def apply_momentum_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Filter short-term trading candidates based on momentum indicators."""
        # Apply RSI filter (oversold/overbought)
        data = data[data['rsi_14'] <= 70]
        # Apply MACD filter (positive momentum)
        data = data[data['macd'] > data['macd_signal']]
        return data
    
    def apply_breakout_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Identify stocks breaking out of key levels for short-term trading."""
        # Filter for stocks breaking above resistance
        data = data[data['close'] > data['resistance']]
        # Confirm with volume surge
        data = data[data['volume'] > data['volume_ma_20'] * 1.5]
        return data
    
    # 🔹 Technical Screening (Long-Term)
    def apply_trend_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Filter long-term investment candidates based on moving averages and money flow."""
        # Price above major moving averages
        data = data[
            (data['close'] > data['ma_50']) & 
            (data['close'] > data['ma_200'])
        ]
        # Positive money flow
        data = data[data['mfi'] > 50]
        return data
    
    def apply_fundamental_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Ensure strong financials for long-term candidates."""
        # Filter for positive earnings growth
        data = data[data['earnings_growth'] > 0]
        # Filter for healthy debt ratios
        data = data[data['debt_to_equity'] < 2.0]
        return data
    
    # 🔹 Final Screening
    def screen_short_term_candidates(self, data: pd.DataFrame) -> list:
        """Run the full short-term screening process and return shortlisted stocks."""
        filtered_data = data.copy()
        
        # Apply fundamental filters
        filtered_data = self.filter_by_market_cap(filtered_data, self.min_market_cap)
        filtered_data = self.filter_by_volume(filtered_data, self.min_volume)
        filtered_data = self.filter_by_volatility(filtered_data, self.min_volatility)
        
        # Apply technical filters for short-term
        filtered_data = self.apply_momentum_filters(filtered_data)
        filtered_data = self.apply_breakout_filters(filtered_data)
        
        return filtered_data['symbol'].tolist()
    
    def screen_long_term_candidates(self, data: pd.DataFrame) -> list:
        """Run the full long-term screening process and return shortlisted stocks."""
        filtered_data = data.copy()
        
        # Apply fundamental filters
        filtered_data = self.filter_by_market_cap(filtered_data, self.min_market_cap)
        filtered_data = self.filter_by_volume(filtered_data, self.min_volume)
        filtered_data = self.apply_fundamental_filters(filtered_data)
        
        # Apply technical filters for long-term
        filtered_data = self.apply_trend_filters(filtered_data)
        
        return filtered_data['symbol'].tolist()
    
    def run(self, data: pd.DataFrame) -> dict:
        """Run both short-term and long-term screening and return candidates."""
        short_term_candidates = self.screen_short_term_candidates(data)
        long_term_candidates = self.screen_long_term_candidates(data)
        return {
            "short_term": short_term_candidates,
            "long_term": long_term_candidates
        }