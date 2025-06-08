from unittest.mock import patch

import pandas as pd
import pytest

from src.analysis_bank.file_handlers import read_csv_transactions, read_excel_transactions


@pytest.fixture
def sample_data():
    return [
        {'Дата': '2023-01-01', 'Сумма': 100, 'Категория': 'Food'},
        {'Дата': '2023-01-02', 'Сумма': 200, 'Категория': 'Transport'}
    ]


def test_read_csv_transactions(sample_data):
    with patch('pandas.read_csv') as mock_read:
        mock_read.return_value = pd.DataFrame(sample_data)
        result = read_csv_transactions('dummy.csv')
        assert result == sample_data


def test_read_excel_transactions(sample_data):
    with patch('pandas.read_excel') as mock_read:
        mock_read.return_value = pd.DataFrame(sample_data)
        result = read_excel_transactions('dummy.xlsx')
        assert result == sample_data
