import time
from functools import wraps
from block_1.common import (
    MyException,
)


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def repeater(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    if i < times:
                        time.sleep(delay)
                    else:
                        raise MyException(e)

        return wrapper

    return repeater

