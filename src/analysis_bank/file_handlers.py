from typing import List, Dict, Union

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Читает транзакции из CSV файла.

    Args:
        file_path: Путь к CSV файлу

    Returns:
        Список словарей с транзакциями
    """
    df = pd.read_csv(file_path)
    return df.to_dict('records')


def read_excel_transactions(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Читает транзакции из Excel файла.

    Args:
        file_path: Путь к Excel файлу

    Returns:
        Список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    return df.to_dict('records')
