from typing import List, Dict, Any

import pytest

from src.bank_operations.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.mark.parametrize("currency,expected_count,expected_id", [
    ("USD", 1, 1),
    ("RUB", 1, 2),
    ("EUR", 0, None)
])
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]],
                            currency: str,
                            expected_count: int,
                            expected_id: int) -> None:
    """Параметризованный тест фильтрации по валюте."""
    result = list(filter_by_currency(sample_transactions, currency))

    assert len(result) == expected_count
    if expected_id:
        assert result[0]["id"] == expected_id
        assert result[0]["Валюта"] == currency


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест извлечения описаний транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2"]


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    """Тест генератора номеров карт."""
    assert list(card_number_generator(start, end)) == expected
