# 🏦 Банковский обработчик операций

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)](https://python-poetry.org/)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-orange.svg)](https://flake8.pycqa.org/)

## 📁 Структура проекта (актуальная)



## 🚀 Быстрый старт

### Установка
```
git clone https://github.com/yourrepo/bank_operations.git
cd bank_operations
poetry install
```
# Полный тестовый прогон
```
poetry run pytest -v --cov=src --cov-report=html
```
## Открыть отчет о покрытии
```
open reports/coverage/index.html
```

### Детали реализации

## Ключевые модули
# Модуль	Функционал	Пример использования
```
masks.py	Маскировка карт/счетов	get_mask_card_number("1234...")
processing.py	Фильтрация и сортировка операций	filter_by_state(ops, "EXECUTED")
widget.py	Основной интерфейс приложения	mask_account_card("Visa 1234")
```
### Пример теста из test_processing.py
```
def test_filter_by_state():
    ops = [{"state": "EXECUTED"}, {"state": "CANCELED"}]
    assert len(filter_by_state(ops)) == 1
```    
# Метрики качества
Покрытие тестами: 80% (см. reports/coverage/80%)
Соответствие PEP 8: 100% (flake8)
Проверка типов: mypy ✅

```
## Модуль generators

### Функции:
```
1. **`filter_by_currency(transactions, currency)`**  
   Фильтрует транзакции по валюте (USD/RUB/EUR)
   
2. **`transaction_descriptions(transactions)`**  
   Возвращает описания транзакций

3. **`card_number_generator(start, end)`**  
   Генерирует номера карт в заданном диапазоне

### Примеры:
```python
# Фильтрация USD транзакций

for tx in filter_by_currency(transactions, "USD"):
    print(tx["id"])

# Генерация номеров карт

for card in card_number_generator(1, 5):
    print(card)  # 0000 0000 0000 0001 ... 0000 0000 0000 0005
```
