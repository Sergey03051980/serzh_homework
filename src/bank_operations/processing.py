from datetime import datetime
from typing import Any, Dict, List, Literal

from bank_operations.decorators import log


def filter_by_state(
        operations: List[Dict[str, Any]],
        state: Literal["EXECUTED", "CANCELED", "PENDING"] = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу.

    Args:
        operations: Список операций
        state: Статус для фильтрации (по умолчанию "EXECUTED")

    Returns:
        Отфильтрованный список операций

    Examples:
        >>> filter_by_state([{"state": "EXECUTED"}])
        [{'state': 'EXECUTED'}]
    """
    if not isinstance(operations, list):
        raise TypeError("Ожидается список операций")
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
        operations: List[Dict[str, Any]],
        reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список операций
        reverse: Если True - новые сначала (по умолчанию)

    Returns:
        Отсортированный список операций

    Examples:
        >>> sort_by_date([{"date": "2023-01-01"}, {"date": "2023-01-02"}])
        [{'date': '2023-01-02'}, {'date': '2023-01-01'}]
    """
    if not isinstance(operations, list):
        raise TypeError("Ожидается список операций")

    def get_date(op):
        try:
            return datetime.fromisoformat(op["date"])
        except (KeyError, ValueError, TypeError):
            return datetime.min if reverse else datetime.max

    return sorted(operations, key=get_date, reverse=reverse)


@log(filename="transactions.log")
def transfer(amount: float, from_acc: str, to_acc: str) -> str:
    """Выполняет перевод денежных средств между счетами.

    Args:
        amount: Сумма перевода
        from_acc: Номер исходного счета
        to_acc: Номер целевого счета

    Returns:
        Подтверждение операции в виде строки
    """

    return f"Transferred {amount} from {from_acc} to {to_acc}"


if __name__ == "__main__":
    print(transfer(100.0, "ACC123", "ACC456"))
