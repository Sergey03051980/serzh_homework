import pandas as pd

from analysis_bank.reports import (spending_by_category, spending_by_weekday,
                                   spending_by_workday)


def test_spending_by_category(sample_dataframe):
    """Test spending_by_category report."""
    result = spending_by_category(sample_dataframe, "Супермаркеты", "2023-05-15")

    assert isinstance(result, pd.DataFrame)
    assert not result.empty


def test_spending_by_weekday(sample_dataframe):
    """Test spending_by_weekday report."""
    result = spending_by_weekday(sample_dataframe, "2023-05-15")

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 7  # 7 days in week


def test_spending_by_workday(sample_dataframe):
    """Test spending_by_workday report."""
    result = spending_by_workday(sample_dataframe, "2023-05-15")

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2  # workday and weekend
