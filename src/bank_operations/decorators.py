import datetime
from functools import wraps
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar

T = TypeVar("T")


def log(
    filename: Optional[str] = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для записи логов. Если None, логи выводятся в консоль.

    Returns:
        Декорированную функцию с логированием.
        :rtype: Callable[[Callable[..., T]], Callable[..., T]]
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> T:
            func_name = func.__name__
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = func(*args, **kwargs)
                log_message = f"{timestamp} - {func_name} - ok. Result: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{timestamp} - {func_name} - error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
