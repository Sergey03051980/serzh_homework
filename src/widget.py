from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Args:
        account_info: Строка с типом и номером карты/счета

    Returns:
        Строка с замаскированным номером

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    if "счет" in account_info.lower():
        parts = account_info.rsplit(" ", 1)
        return f"{parts[0]} {get_mask_account(parts[1])}"
    else:
        parts = account_info.rsplit(" ", 1)
        return f"{parts[0]} {get_mask_card_number(parts[1])}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "11.03.2024"

    Args:
        date_str: Строка с датой и временем

    Returns:
        Строка с датой в формате ДД.ММ.ГГГГ
    """
    from datetime import datetime

    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
