import functools
import json
import logging
from datetime import datetime, timedelta
from typing import Any, Callable, Optional

import pandas as pd

logger = logging.getLogger(__name__)


def report_decorator(filename: Optional[str] = None) -> Callable:
    """Decorator to save report results to file.

    Args:
        filename: Optional filename to save report

    Returns:
        Decorator function
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)

            # Determine filename
            report_filename = filename or f"{func.__name__}_report.json"

            # Save to file
            try:
                with open(report_filename, "w") as f:
                    if isinstance(result, pd.DataFrame):
                        json.dump(result.to_dict(orient="records"), f)
                    else:
                        json.dump(result, f)
                logger.info(f"Report saved to {report_filename}")
            except Exception as e:
                logger.error(f"Error saving report: {e}")

            return result

        return wrapper

    return decorator


@report_decorator()
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = None
) -> pd.DataFrame:
    """Calculate spending by category for last 3 months.

    Args:
        transactions: DataFrame with transactions
        category: Category to analyze
        date: Reference date (default: current date)

    Returns:
        DataFrame with spending by month
    """
    try:
        if date is None:
            date_obj = datetime.now()
        else:
            date_obj = datetime.strptime(date, "%Y-%m-%d")

        end_date = date_obj
        start_date = end_date - timedelta(days=90)

        # Filter transactions
        filtered = transactions[
            (transactions["Дата операции"] >= start_date)
            & (transactions["Дата операции"] <= end_date)
            & (transactions["Категория"] == category)
        ]

        # Group by month
        result = (
            filtered.groupby(filtered["Дата операции"].dt.to_period("M"))[
                "Сумма платежа"
            ]
            .sum()
            .reset_index()
        )

        result["Дата операции"] = result["Дата операции"].astype(str)
        return result
    except Exception as e:
        logger.error(f"Error in spending_by_category: {e}")
        raise


@report_decorator()
def spending_by_weekday(
    transactions: pd.DataFrame, date: Optional[str] = None
) -> pd.DataFrame:
    """Calculate average spending by weekday for last 3 months.

    Args:
        transactions: DataFrame with transactions
        date: Reference date (default: current date)

    Returns:
        DataFrame with average spending by weekday
    """
    try:
        if date is None:
            date_obj = datetime.now()
        else:
            date_obj = datetime.strptime(date, "%Y-%m-%d")

        end_date = date_obj
        start_date = end_date - timedelta(days=90)

        # Filter transactions
        filtered = transactions[
            (transactions["Дата операции"] >= start_date)
            & (transactions["Дата операции"] <= end_date)
        ]

        # Calculate average by weekday
        filtered["weekday"] = filtered["Дата операции"].dt.weekday
        result = filtered.groupby("weekday")["Сумма платежа"].mean().reset_index()

        # Map weekday numbers to names
        weekday_names = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        result["weekday"] = result["weekday"].map(weekday_names)

        return result
    except Exception as e:
        logger.error(f"Error in spending_by_weekday: {e}")
        raise


@report_decorator("workday_spending_report.json")
def spending_by_workday(
    transactions: pd.DataFrame, date: Optional[str] = None
) -> pd.DataFrame:
    """Calculate average spending on workdays vs weekends.

    Args:
        transactions: DataFrame with transactions
        date: Reference date (default: current date)

    Returns:
        DataFrame with average spending by day type
    """
    try:
        if date is None:
            date_obj = datetime.now()
        else:
            date_obj = datetime.strptime(date, "%Y-%m-%d")

        end_date = date_obj
        start_date = end_date - timedelta(days=90)

        # Filter transactions
        filtered = transactions[
            (transactions["Дата операции"] >= start_date)
            & (transactions["Дата операции"] <= end_date)
        ]

        # Classify as workday or weekend
        filtered["day_type"] = filtered["Дата операции"].apply(
            lambda x: "weekend" if x.weekday() >= 5 else "workday"
        )

        # Calculate averages
        result = filtered.groupby("day_type")["Сумма платежа"].mean().reset_index()
        return result
    except Exception as e:
        logger.error(f"Error in spending_by_workday: {e}")
        raise
