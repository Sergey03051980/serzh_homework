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

## Установка

```

 #Теперь пакет называется__/bank_operations/
 
```

# 🏦 Банковский обработчик

## 🚀 Быстрый старт

```bash
git clone https://github.com/your-repo.git
cd project
poetry install
poetry run pytest
```

**🔍 Основные функции**

Маскировка данных

```python

from bank_operations.masks import get_mask_card_number

get_mask_card_number("1234567812345678")  # → "1234 56** **** 5678"
```

Логирование операции

``` python

from bank_operations.decorators import log

@log(filename="ops.log")
def transfer(amount, from_acc, to_acc):
    return f"Перевод {amount}"
```

Обработка операций

```python
from bank_operations.processing import filter_by_state

filter_by_state(operations, "EXECUTED")
```

📊 Тестирование

```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html  # Отчёт покрытия
```

🛠 Утилиты

```bash
flake8 src    # Проверка стиля
mypy src      # Проверка типов

````

# PythonProject

Анализ банковских транзакций

## 📌 Возможности проекта

- Загрузка транзакций из различных форматов:
    - JSON (базовый формат)
    - CSV
    - Excel (XLSX)
- Анализ финансовых операций
- Генерация отчетов
- Фильтрация транзакций по датам и категориям

## 🛠 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/PythonProject.git
   cd PythonProject
   ```

Установите зависимости через Poetry:

```
poetry install
```

Активируйте виртуальное окружение:

```
poetry shell
```

📂 Поддерживаемые форматы файлов
Проект работает со следующими форматами данных:

```
csv
Дата_операции,Категория,Сумма_операции
2023-01-01,Продукты,1500.50
2023-01-02,Транспорт,500.00
Excel (XLSX)
```

Пример структуры файла ***transactions.csv***:

```
Дата_операции Категория Сумма_операции
2023-01-01 Продукты 1500.50

```

🧪 Тестирование

```

Запуск тестов:

```

pytest tests/

```

Проверка покрытия:

```

pytest --cov=src tests/

```

***Пример использования**

```pathon

from src.analysis_bank.file_handlers import read_csv_transactions

transactions = read_csv_transactions('data/transactions.csv')
for transaction in transactions:
    print(f"{transaction['Дата_операции']}: {transaction['Категория']} - {transaction['Сумма_операции']}")
```