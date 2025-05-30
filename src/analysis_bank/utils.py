import logging
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_transactions(filepath: str) -> pd.DataFrame:
    """Load transactions from Excel file.

    Args:
        filepath: Path to Excel file with transactions

    Returns:
        DataFrame with transactions data
    """
    try:
        df = pd.read_excel(filepath)
        logger.info("Transactions loaded successfully")
        return df
    except Exception as e:
        logger.error(f"Error loading transactions: {e}")
        raise


def filter_transactions_by_date(
    df: pd.DataFrame, date_str: str, date_range: str = "M"
) -> pd.DataFrame:
    """Filter transactions by date range.

    Args:
        df: DataFrame with transactions
        date_str: Date in format 'YYYY-MM-DD HH:MM:SS'
        date_range: Range to filter ('W', 'M', 'Y', 'ALL')

    Returns:
        Filtered DataFrame
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        df["Дата операции"] = pd.to_datetime(df["Дата операции"])

        if date_range == "W":
            start_date = date - pd.Timedelta(days=date.weekday())
        elif date_range == "M":
            start_date = date.replace(day=1)
        elif date_range == "Y":
            start_date = date.replace(month=1, day=1)
        elif date_range == "ALL":
            return df[df["Дата операции"] <= date]

        return df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= date)]
    except Exception as e:
        logger.error(f"Error filtering transactions: {e}")
        raise


def get_greeting(time: datetime) -> str:
    """Return greeting based on time of day.

    Args:
        time: Datetime object

    Returns:
        Greeting string
    """
    hour = time.hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 23:
        return "Добрый вечер"
    return "Доброй ночи"


def fetch_currency_rates(currencies: List[str]) -> List[Dict[str, Any]]:
    """Fetch currency rates from API.

    Args:
        currencies: List of currency codes to fetch

    Returns:
        List of dictionaries with currency rates
    """
    try:
        # Example API - replace with actual implementation
        results = []
        for currency in currencies:
            # Mock implementation - replace with real API call
            rate = 75.0 if currency == "USD" else 85.0
            results.append({"currency": currency, "rate": rate})
        return results
    except Exception as e:
        logger.error(f"Error fetching currency rates: {e}")
        return []


def fetch_stock_prices(stocks: List[str]) -> List[Dict[str, Any]]:
    """Fetch stock prices from API.

    Args:
        stocks: List of stock symbols to fetch

    Returns:
        List of dictionaries with stock prices
    """
    try:
        # Example API - replace with actual implementation
        results = []
        for stock in stocks:
            # Mock implementation - replace with real API call
            price = 150.0 if stock == "AAPL" else 3000.0
            results.append({"stock": stock, "price": price})
        return results
    except Exception as e:
        logger.error(f"Error fetching stock prices: {e}")
        return []
