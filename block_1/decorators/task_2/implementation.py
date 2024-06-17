from functools import wraps
from block_1.common import (
    MyException,
)


def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        for arg in args:
            if (not isinstance(arg, int)) or arg < 0:
                raise MyException
        base_result = function(*args, **kwargs)

        return base_result

    return wrapper
