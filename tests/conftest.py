from datetime import datetime
from typing import Dict, List, Any

import pandas as pd
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
    """Фикстура предоставляет тестовые данные транзакций.

    Returns:
        List[Dict[str, Any]]: Список транзакций с разными валютами и описаниями
        Пример структуры:
        [
            {
                "id": 1,
                "Дата_операции": "2023-05-01",
                "Валюта": "USD",
                "Описание": "Payment 1"
            },
            ...
        ]
    """
    return [
        {
            "id": 1,
            "Дата_операции": "2023-05-01",
            "Валюта": "USD",
            "Описание": "Payment 1",
            "Сумма": 100.50
        },
        {
            "id": 2,
            "Дата_операции": "2023-05-02",
            "Валюта": "RUB",
            "Описание": "Payment 2",
            "Сумма": 5000.00
        }
    ]


@pytest.fixture
def edge_cases() -> List[Dict[str, Any]]:
    """Фикстура для тестирования крайних случаев.

    Returns:
        List[Dict[str, Any]]: Список проблемных транзакций:
        - Транзакция с None в валюте
        - Пустой словарь
        - Транзакция с несуществующей валютой
    """
    return [
        {"Валюта": None, "Описание": "No currency"},
        {},
        {"Валюта": "EUR", "Описание": "Euro payment"}
    ]


@pytest.fixture
def sample_dataframe():
    data = [
        {"id": 1, "Дата_операции": "2023-05-01", "Валюта": "USD", "Описание": "Payment 1", "Сумма": 100.5},
        {"id": 2, "Дата_операции": "2023-05-02", "Валюта": "RUB", "Описание": "Payment 2", "Сумма": 5000.0}
    ]
    df = pd.DataFrame(data)
    df["Дата_операции"] = pd.to_datetime(df["Дата_операции"])
    return df


@pytest.fixture
def phone_transactions() -> List[Dict[str, Any]]:
    """Fixture with transactions containing phone numbers."""
    return [
        {
            "Дата_операции": "2023-05-01",
            "Категория": "Мобильная связь",
            "Описание": "Пополнение МТС +7 921 123-45-67",
            "Сумма_операции": 500.0,
        },
        {
            "Дата_операции": "2023-05-02",
            "Категория": "Другое",
            "Описание": "Оплата услуг",
            "Сумма_операции": 100.0,
        },
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


@pytest.fixture
def sample_csv(tmp_path):
    csv_data = """Дата,Описание,Сумма
2023-01-01,Покупка,1000
2023-01-02,Такси,500"""
    file = tmp_path / "test.csv"
    file.write_text(csv_data)
    return str(file)
