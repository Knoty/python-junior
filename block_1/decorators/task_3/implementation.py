from functools import wraps


count = 0


def counter(function):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        global count
        count += 1
        function(*args, **kwargs)

        return count

    return wrapper
