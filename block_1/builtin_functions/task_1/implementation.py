from block_1.common import (
    MyException
)


class Value:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        try:
            return self.value + other
        except Exception:
            raise MyException(Exception)

    def __sub__(self, other):
        try:
            return self.value - other
        except Exception:
            raise MyException(Exception)

    def __mul__(self, other):
        try:
            return self.value * other
        except Exception:
            raise MyException(Exception)

    def __truediv__(self, other):
        try:
            return self.value / other
        except Exception:
            raise MyException(Exception)