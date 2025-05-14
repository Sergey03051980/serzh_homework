import pytest
from src.pythonproject.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def sample_card_numbers():
    return ["1234567890123456", "1111222233334444", "123", "abcdefghijklmnop"]


def test_get_mask_card_number(sample_card_numbers):
    # Тестируем валидные номера
    assert get_mask_card_number(sample_card_numbers[0]) == "1234 56** **** 3456"

    # Тестируем ошибки
    with pytest.raises(ValueError):
        get_mask_card_number(sample_card_numbers[2])
