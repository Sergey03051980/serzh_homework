# My Project My homework

# Обработка банковских операций

Модуль для фильтрации и сортировки банковских операций.

## Функционал

### `filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]`
Фильтрует список операций по значению ключа 'state'.

**Параметры:**
- `operations`: Список словарей с банковскими операциями
- `state`: Значение состояния для фильтрации (по умолчанию 'EXECUTED')

**Возвращает:**
- Новый список операций с указанным состоянием

**Пример:**
```python
operations = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'CANCELED'}
]
filter_by_state(operations)  # [{'id': 1, 'state': 'EXECUTED'}]

operations = [
    {'id': 1, 'date': '2023-01-01'},
    {'id': 2, 'date': '2023-01-02'}
]
sort_by_date(operations)  # [{'id': 2, 'date': '2023-01-02'}, {'id': 1, 'date': '2023-01-01'}]
```
***Установка и запуск***

**Клонируйте репозиторий:**
```
git clone git@github.com:Sergey03051980/serzh_homework.git
cd serzh_homework
```
**Установите зависимости:**
```
pip install -r requirements.txt
```
**Запустите тесты:**
```
pytest tests/ -v
```

**Запууск тестов:**
```
pytest tests/test_processing.py -v
```



