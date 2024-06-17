from functools import wraps
import time


def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        base_result = function(*args, **kwargs)
        print("%s секунд" % (time.time() - start_time))

        return base_result

    return wrapper
