from src.widget import mask_account_card, get_date

# Примеры работы функций
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))       # Счет **4305
print(get_date("2024-03-11T02:26:18.671407"))              # 11.03.2024