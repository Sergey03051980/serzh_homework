import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T00:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02T00:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03T00:00:00'},
        {'id': 4, 'state': 'CANCELED', 'date': '2023-01-04T00:00:00'},
        {'id': 5, 'state': 'PENDING', 'date': '2023-01-05T00:00:00'},
    ]


def test_filter_by_state(sample_operations):
    # Тест фильтрации по умолчанию (EXECUTED)
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(op['state'] == 'EXECUTED' for op in result)

    # Тест фильтрации по CANCELED
    result = filter_by_state(sample_operations, 'CANCELED')
    assert len(result) == 2
    assert all(op['state'] == 'CANCELED' for op in result)

    # Тест пустого ввода
    assert filter_by_state([]) == []


def test_sort_by_date(sample_operations):
    # Сортировка по убыванию (новые сначала)
    sorted_desc = sort_by_date(sample_operations)
    assert sorted_desc[0]['id'] == 5
    assert sorted_desc[-1]['id'] == 1

    # Сортировка по возрастанию (старые сначала)
    sorted_asc = sort_by_date(sample_operations, reverse=False)
    assert sorted_asc[0]['id'] == 1
    assert sorted_asc[-1]['id'] == 5

    # Тест с пустым списком
    assert sort_by_date([]) == []

    # Дополнительные тесты функций
if __name__ == "__main__":
    # Пример данных для тестирования
    test_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    # Тестирование filter_by_state
    print("EXECUTED операции:")
    print(filter_by_state(test_data))  # По умолчанию 'EXECUTED'

    print("\nCANCELED операции:")
    print(filter_by_state(test_data, 'CANCELED'))

    # Тестирование sort_by_date
    print("\nСортировка по убыванию даты:")
    print(sort_by_date(test_data))  # По умолчанию reverse=True

    print("\nСортировка по возрастанию даты:")
    print(sort_by_date(test_data, reverse=False))

