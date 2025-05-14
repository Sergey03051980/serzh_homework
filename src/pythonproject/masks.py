def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX

    Args:
        card_number: Номер карты (16 цифр)

    Returns:
        Маскированный номер карты

    Raises:
        ValueError: Если номер карты невалидный
    """
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX

    Args:
        account_number: Номер счета (минимум 4 цифры)

    Returns:
        Маскированный номер счета

    Raises:
        ValueError: Если номер счета невалидный
    """
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
