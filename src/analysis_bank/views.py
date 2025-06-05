import logging
from datetime import datetime
from typing import Any, Dict

from analysis_bank.utils import (
    fetch_currency_rates,
    fetch_stock_prices,
    filter_transactions_by_date,
    get_greeting,
    load_transactions,
)

logger = logging.getLogger(__name__)


def home_page(date_str: str) -> Dict[str, Any]:
    """Generate data for home page.

    Args:
        date_str: Date in format 'YYYY-MM-DD HH:MM:SS'

    Returns:
        Dictionary with data for home page
    """
    try:
        # Load transactions
        df = load_transactions("data/operations.xlsx")

        # Filter transactions
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        df_filtered = filter_transactions_by_date(df, date_str)

        # Generate greeting
        greeting = get_greeting(date_obj)

        # Calculate card statistics
        cards = []
        for card in df_filtered["Номер карты"].unique():
            card_df = df_filtered[df_filtered["Номер карты"] == card]
            total_spent = card_df["Сумма платежа"].sum()
            cashback = total_spent / 100
            cards.append(
                {
                    "last_digits": str(card)[-4:],
                    "total_spent": round(total_spent, 2),
                    "cashback": round(cashback, 2),
                }
            )

        # Get top 5 transactions
        top_transactions = df_filtered.nlargest(5, "Сумма платежа")
        top_transactions_list = []
        for _, row in top_transactions.iterrows():
            top_transactions_list.append(
                {
                    "date": row["Дата операции"].strftime("%d.%m.%Y"),
                    "amount": row["Сумма платежа"],
                    "category": row["Категория"],
                    "description": row["Описание"],
                }
            )

        # Get currency rates and stock prices
        currency_rates = fetch_currency_rates(["USD", "EUR"])
        stock_prices = fetch_stock_prices(["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"])

        return {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_transactions_list,
            "currency_rates": currency_rates,
            "stock_prices": stock_prices,
        }
    except Exception as e:
        logger.error(f"Error generating home page data: {e}")
        raise


def events_page(date_str: str, date_range: str = "M") -> Dict[str, Any]:
    """Generate data for events page.

    Args:
        date_str: Date in format 'YYYY-MM-DD HH:MM:SS'
        date_range: Date range ('W', 'M', 'Y', 'ALL')

    Returns:
        Dictionary with data for events page
    """
    try:
        # Load and filter transactions
        df = load_transactions("data/operations.xlsx")
        df_filtered = filter_transactions_by_date(df, date_str, date_range)

        # Calculate expenses
        expenses_df = df_filtered[df_filtered["Сумма платежа"] > 0]
        expenses_total = round(expenses_df["Сумма платежа"].sum())

        # Group by category for main expenses
        main_expenses = expenses_df[
            ~expenses_df["Категория"].isin(["Наличные", "Переводы"])
        ]
        main_categories = main_expenses.groupby("Категория")["Сумма платежа"].sum()
        main_categories = main_categories.sort_values(ascending=False)

        # Get top 7 categories, sum the rest as "Остальное"
        if len(main_categories) > 7:
            other_sum = main_categories[7:].sum()
            main_categories = main_categories[:7]
            main_categories["Остальное"] = other_sum

        main_expenses_list = [
            {"category": k, "amount": round(v)} for k, v in main_categories.items()
        ]

        # Calculate transfers and cash
        transfers_cash = expenses_df[
            expenses_df["Категория"].isin(["Наличные", "Переводы"])
        ]
        transfers_cash_grouped = transfers_cash.groupby("Категория")[
            "Сумма платежа"
        ].sum()
        transfers_cash_list = [
            {"category": k, "amount": round(v)}
            for k, v in transfers_cash_grouped.items()
        ]

        # Calculate income
        income_df = df_filtered[df_filtered["Сумма платежа"] < 0]
        income_total = round(abs(income_df["Сумма платежа"].sum()))

        # Group income by category
        income_categories = income_df.groupby("Категория")["Сумма платежа"].sum()
        income_categories = abs(income_categories).sort_values(ascending=False)
        income_list = [
            {"category": k, "amount": round(v)} for k, v in income_categories.items()
        ]

        # Get currency rates and stock prices
        currency_rates = fetch_currency_rates(["USD", "EUR"])
        stock_prices = fetch_stock_prices(["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"])

        return {
            "expenses": {
                "total_amount": expenses_total,
                "main": main_expenses_list,
                "transfers_and_cash": transfers_cash_list,
            },
            "income": {"total_amount": income_total, "main": income_list},
            "currency_rates": currency_rates,
            "stock_prices": stock_prices,
        }
    except Exception as e:
        logger.error(f"Error generating events page data: {e}")
        raise
