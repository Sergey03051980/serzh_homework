from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Transaction:
    """Модель банковской транзакции"""
    Дата_операции: str
    Категория: str
    Описание: str = ""
    Сумма_операции: str = "0"
    Кешбэк: float = 0.0
    Отправитель: str = ""
    Получатель: str = ""

    def get_date(self) -> Optional[datetime]:
        """Конвертирует строковую дату в объект datetime"""
        try:
            return datetime.strptime(self.Дата_операции, "%Y-%m-%d")
        except ValueError:
            return None
