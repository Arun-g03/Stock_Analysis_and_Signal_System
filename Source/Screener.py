import pandas as pd

class StockScreener:
    def __init__(self, min_market_cap: float, min_volume: int, min_volatility: float):
        """Initialize screener with fundamental and technical thresholds."""
    
    # 🔹 Fundamental Screening
    def filter_by_market_cap(self, data: pd.DataFrame, min_cap: float) -> pd.DataFrame:
        """Filter stocks based on market capitalization."""
    
    def filter_by_volume(self, data: pd.DataFrame, min_volume: int) -> pd.DataFrame:
        """Filter out stocks with low trading volume."""
    
    def filter_by_volatility(self, data: pd.DataFrame, min_volatility: float) -> pd.DataFrame:
        """Remove stocks with very low price movement."""
    
    # 🔹 Technical Screening (Short-Term)
    def apply_momentum_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Filter short-term trading candidates based on momentum indicators."""
    
    def apply_breakout_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Identify stocks breaking out of key levels for short-term trading."""
    
    # 🔹 Technical Screening (Long-Term)
    def apply_trend_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Filter long-term investment candidates based on moving averages and money flow."""
    
    def apply_fundamental_filters(self, data: pd.DataFrame) -> pd.DataFrame:
        """Ensure strong financials for long-term candidates."""
    
    # 🔹 Final Screening
    def screen_short_term_candidates(self) -> list:
        """Run the full short-term screening process and return shortlisted stocks."""
    
    def screen_long_term_candidates(self) -> list:
        """Run the full long-term screening process and return shortlisted stocks."""
