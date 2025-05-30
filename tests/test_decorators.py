import os

import pytest

from bank_operations.decorators import log


def test_log_to_file(tmp_path):
    """Тест записи логов в файл."""
    filename = os.path.join(tmp_path, "test.log")

    @log(filename=filename)
    def add(a: int, b: int) -> int:
        return a + b

    add(2, 3)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert "add - ok. Result: 5" in content


def test_log_to_console(capsys):
    """Тест вывода логов в консоль."""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    divide(10, 2)
    captured = capsys.readouterr()
    assert "divide - ok. Result: 5.0" in captured.out


def test_log_error(capsys):
    """Тест логирования ошибок."""

    @log()
    def fail() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    assert "fail - error: ValueError" in captured.out
