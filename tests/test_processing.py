import pytest
from datetime import datetime, timedelta
from src.pythonproject.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    """Фикстура с тестовыми данными операций"""
    base_date = datetime.now()
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": (base_date - timedelta(days=1)).isoformat(),
            "description": "Payment 1",
            "operationAmount": {"amount": "100", "currency": {"name": "USD"}}
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": (base_date - timedelta(days=2)).isoformat(),
            "description": "Payment 2",
            "operationAmount": {"amount": "200", "currency": {"name": "EUR"}}
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": (base_date - timedelta(days=3)).isoformat(),
            "description": "Payment 3",
            "operationAmount": {"amount": "300", "currency": {"name": "RUB"}}
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": (base_date - timedelta(days=4)).isoformat(),
            "description": "Payment 4",
            "operationAmount": {"amount": "400", "currency": {"name": "GBP"}}
        }
    ]

def test_filter_by_state_executed(sample_operations):
    """Тест фильтрации по EXECUTED"""
    result = filter_by_state(sample_operations, "EXECUTED")
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)

def test_filter_by_state_canceled(sample_operations):
    """Тест фильтрации по CANCELED"""
    result = filter_by_state(sample_operations, "CANCELED")
    assert len(result) == 1
    assert all(op["state"] == "CANCELED" for op in result)

def test_filter_by_state_default(sample_operations):
    """Тест фильтрации со значением по умолчанию"""
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)

def test_filter_by_state_empty_input():
    """Тест с пустым входным списком"""
    assert filter_by_state([]) == []

def test_sort_by_date_descending(sample_operations):
    """Тест сортировки по убыванию даты"""
    result = sort_by_date(sample_operations)
    dates = [datetime.fromisoformat(op["date"]) for op in result]
    assert dates == sorted(dates, reverse=True)

def test_sort_by_date_ascending(sample_operations):
    """Тест сортировки по возрастанию даты"""
    result = sort_by_date(sample_operations, reverse=False)
    dates = [datetime.fromisoformat(op["date"]) for op in result]
    assert dates == sorted(dates)

def test_sort_by_date_empty_input():
    """Тест сортировки пустого списка"""
    assert sort_by_date([]) == []

@pytest.mark.parametrize("operations, expected", [
    ([], []),
    ([{"date": "2023-01-01"}], [{"date": "2023-01-01"}]),
])
def test_sort_by_date_edge_cases(operations, expected):
    """Тест граничных случаев сортировки"""
    assert sort_by_date(operations) == expected