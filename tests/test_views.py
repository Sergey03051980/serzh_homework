from analysis_bank.views import events_page, home_page


def test_home_page_structure(sample_dataframe, mocker):
    """Test home_page returns correct structure."""
    mocker.patch("src.utils.load_transactions", return_value=sample_dataframe)
    mocker.patch("src.utils.fetch_currency_rates", return_value=[])
    mocker.patch("src.utils.fetch_stock_prices", return_value=[])

    result = home_page("2023-05-15 12:00:00")

    assert isinstance(result, dict)
    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "currency_rates" in result
    assert "stock_prices" in result


def test_events_page_structure(sample_dataframe, mocker):
    """Test events_page returns correct structure."""
    mocker.patch("src.utils.load_transactions", return_value=sample_dataframe)
    mocker.patch("src.utils.fetch_currency_rates", return_value=[])
    mocker.patch("src.utils.fetch_stock_prices", return_value=[])

    result = events_page("2023-05-15 12:00:00")

    assert isinstance(result, dict)
    assert "expenses" in result
    assert "income" in result
    assert "currency_rates" in result
    assert "stock_prices" in result
