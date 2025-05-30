from datetime import timedelta
from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_card_numbers() -> List[str]:
    """Фикстура с валидными и невалидными номерами карт"""
    return [
        "1234567890123456",  # valid
        "1111222233334444",  # valid
        "123",  # invalid (short)
        "abcdefghijklmnop",  # invalid (letters)
    ]


@pytest.fixture
def sample_account_numbers() -> List[str]:
    """Фикстура с валидными и невалидными номерами счетов"""
    return [
        "1234567890123456",  # valid
        "1234",  # valid (min length)
        "12",  # invalid (short)
        "abcdef",  # invalid (letters)
    ]


@pytest.fixture
def sample_account_strings() -> List[str]:
    """Фикстура с валидными и невалидными строками карт/счетов"""
    return [
        "Visa Platinum 1234567890123456",
        "Счет 1234567890123456",
        "Maestro 1234567890123456",
        "Invalid String Without Number",
        "Счет 123",  # invalid
    ]


@pytest.fixture
def sample_dates() -> List[str]:
    """Фикстура с валидными и невалидными датами"""
    return [
        "2023-01-01",
        "2023-12-31T23:59:59.999999",
        "invalid-date",
        "",
    ]


@pytest.fixture
def sample_operations() -> List[Dict]:
    """Фикстура с операциями для тестирования processing.py"""
    base_date = datetime.now()
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": (base_date - timedelta(days=1)).isoformat(),
            "description": "Visa 1234567890123456",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": (base_date - timedelta(days=2)).isoformat(),
            "description": "Счет 1234567890123456",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": (base_date - timedelta(days=3)).isoformat(),
            "description": "MasterCard 1234567890123456",
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": "invalid-date",  # специально невалидная
            "description": "Invalid Operation",
        },
    ]


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100.00", "currency": {"code": "USD"}},
            "description": "Payment 1",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200.00", "currency": {"code": "EUR"}},
            "description": "Payment 2",
        },
    ]


@pytest.fixture
def edge_cases() -> List[Dict[str, Any]]:
    return [{}, {"operationAmount": {}}, {"operationAmount": {"currency": {}}}, None]


from datetime import datetime
from typing import Any, Dict, List

import pandas as pd
import pytest


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Fixture with sample transactions data."""
    return [
        {
            "Дата операции": "2023-05-01",
            "Номер карты": "1234567890123456",
            "Сумма платежа": 100.0,
            "Категория": "Супермаркеты",
            "Описание": "Покупка в магазине",
            "Кешбэк": 1.0,
        },
        {
            "Дата операции": "2023-05-02",
            "Номер карты": "1234567890123456",
            "Сумма платежа": 50.0,
            "Категория": "Кафе",
            "Описание": "Обед в кафе",
            "Кешбэк": 0.5,
        },
        {
            "Дата операции": "2023-04-15",
            "Номер карты": "9876543210987654",
            "Сумма платежа": 200.0,
            "Категория": "Переводы",
            "Описание": "Перевод Ивану П.",
            "Кешбэк": 0.0,
        },
        {
            "Дата операции": "2023-04-10",
            "Номер карты": "9876543210987654",
            "Сумма платежа": -500.0,
            "Категория": "Пополнение",
            "Описание": "Пополнение счета",
            "Кешбэк": 0.0,
        },
        {
            "Дата операции": "2023-03-20",
            "Номер карты": "1234567890123456",
            "Сумма платежа": 75.0,
            "Категория": "Супермаркеты",
            "Описание": "Покупка в магазине",
            "Кешбэк": 0.75,
        },
    ]


@pytest.fixture
def sample_dataframe(sample_transactions: List[Dict[str, Any]]) -> pd.DataFrame:
    """Fixture with sample DataFrame."""
    return pd.DataFrame(sample_transactions)


@pytest.fixture
def phone_transactions() -> List[Dict[str, Any]]:
    """Fixture with transactions containing phone numbers."""
    return [
        {
            "Дата операции": "2023-05-01",
            "Категория": "Мобильная связь",
            "Описание": "Пополнение МТС +7 921 123-45-67",
            "Сумма платежа": 500.0,
        },
        {
            "Дата операции": "2023-05-02",
            "Категория": "Другое",
            "Описание": "Оплата услуг",
            "Сумма платежа": 100.0,
        },
    ]


import pytest


@pytest.fixture
def sample_transactions():
    return [{"amount": 100, "recipient": "John"}, ...]


import pytest


@pytest.fixture
def sample_transactions():
    return [
        {
            "Дата_операции": "2023-05-01",
            "Категория": "Супермаркеты",
            "Сумма_операции": "1000",
            "Кешбэк": 1.0,
            "Описание": "Покупки в магазине"
        }
    ]


@pytest.fixture
def phone_transactions():
    return [
        {
            "Дата_операции": "2023-05-01",
            "Категория": "Мобильная связь",
            "Описание": "Пополнение +79161234567",
            "Сумма_операции": "500"
        }
    ]
