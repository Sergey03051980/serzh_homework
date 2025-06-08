from typing import Any, List, Dict

from analysis_bank.models import Transaction
from analysis_bank.services import profitable_cashback_categories, investment_bank


def prepare_transactions(raw_data: List[Dict[str, Any]]) -> List[Transaction]:
    return [
        Transaction(
            Дата_операции=str(item.get('Дата_операции', '')),
            Категория=str(item.get('Категория', '')),
            Описание=str(item.get('Описание', '')),
            Сумма_операции=str(item.get('Сумма_операции', '0')),
            Кешбэк=float(item.get('Кешбэк', 0)),
            Отправитель=str(item.get('Отправитель', '')),
            Получатель=str(item.get('Получатель', ''))
        )
        for item in raw_data
    ]


def main():
    # Пример данных
    raw_transactions = [
        {
            'Дата_операции': '2023-01-15',
            'Категория': 'Продукты',
            'Сумма_операции': '1500',
            'Кешбэк': 75.0,
            'Отправитель': 'Иванов И.',
            'Получатель': 'Магазин Пятерочка'
        },
        # ... другие транзакции
    ]

    # Преобразуем данные
    transactions = prepare_transactions(raw_transactions)

    # Анализ кешбэка
    cashback = profitable_cashback_categories(transactions, 2023, 1)
    print(f"Кешбэк по категориям: {cashback}")

    # Анализ инвестиций
    savings = investment_bank("2023-01", transactions, 100)
    print(f"Сбережения от округления: {savings}")


if __name__ == "__main__":
    main()
