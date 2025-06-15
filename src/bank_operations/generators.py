from typing import List, Dict, Any, Generator, Iterator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по указанной валюте.

    Args:
        transactions: Список транзакций (словарей)
        currency: Код валюты для фильтрации (например, "USD", "RUB")

    Returns:
        Iterator[Dict[str, Any]]: Итератор по отфильтрованным транзакциям

    Example:
        >>> list(filter_by_currency([{"Валюта": "USD"}], "USD"))
        [{"Валюта": "USD"}]
    """
    return (t for t in transactions if t.get("Валюта") == currency)


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Извлекает описания из списка транзакций.

    Args:
        transactions: Список транзакций

    Returns:
        Iterator[str]: Итератор по описаниям транзакций

    Raises:
        KeyError: Если у транзакции отсутствует поле "Описание"

    Example:
        >>> list(transaction_descriptions([{"Описание": "Test"}]))
        ["Test"]
    """
    return (t["Описание"] for t in transactions)


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start: Начальный номер (включительно)
        end: Конечный номер (включительно)

    Returns:
        Generator[str, None, None]: Генератор номеров карт в формате 0000 0000 0000 XXXX

    Raises:
        ValueError: Если start > end

    Example:
        >>> list(card_number_generator(1, 2))
        ['0000 0000 0000 0001', '0000 0000 0000 0002']
    """
    if start > end:
        raise ValueError("Start value cannot be greater than end value")

    for i in range(start, end + 1):
        yield f"0000 0000 0000 {i:04d}"
