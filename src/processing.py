from typing import List, Dict, Any, Optional
from datetime import datetime


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Args:
        operations: Список словарей с банковскими операциями.
                   Каждая операция должна содержать ключ 'state'.
        state: Значение состояния для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Новый список операций, где каждая операция имеет указанное состояние.

    Raises:
        KeyError: Если в какой-либо операции отсутствует ключ 'state'.

    Examples:
        >>> operations = [
        ...     {'id': 1, 'state': 'EXECUTED'},
        ...     {'id': 2, 'state': 'CANCELED'}
        ... ]
        >>> filter_by_state(operations)
        [{'id': 1, 'state': 'EXECUTED'}]
    """
    if not operations:
        return []

    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате (ключ 'date').

    Args:
        operations: Список словарей с банковскими операциями.
                   Каждая операция должна содержать ключ 'date' в формате ISO.
        reverse: Если True - сортировка по убыванию (новые сначала),
                 если False - по возрастанию (старые сначала).

    Returns:
        Новый список операций, отсортированный по дате.

    Raises:
        KeyError: Если в какой-либо операции отсутствует ключ 'date'.
        ValueError: Если дата в неверном формате.

    Examples:
        >>> operations = [
        ...     {'id': 1, 'date': '2023-01-01'},
        ...     {'id': 2, 'date': '2023-01-02'}
        ... ]
        >>> sort_by_date(operations)
        [{'id': 2, 'date': '2023-01-02'}, {'id': 1, 'date': '2023-01-01'}]
    """
    if not operations:
        return []

    def get_date(op: Dict[str, Any]) -> datetime:
        try:
            return datetime.fromisoformat(op['date'])
        except KeyError:
            raise KeyError(f"Операция {op.get('id', 'без ID')} не содержит ключа 'date'")
        except ValueError:
            raise ValueError(f"Неверный формат даты в операции {op.get('id', 'без ID')}: {op['date']}")

    return sorted(operations, key=get_date, reverse=reverse)



