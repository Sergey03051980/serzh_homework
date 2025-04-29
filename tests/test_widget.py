
from src.widget import mask_account_card, get_date

def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-31T23:59:59.999999") == "31.12.2023"

if __name__ == '__main__':

    account_number = str(input())
    print(get_mask_account(account_number))
