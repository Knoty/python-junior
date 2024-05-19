from datetime import (
    date,
)

from block_1.flow_control.task_3.implementation import (
    get_days_count_by_month,
)


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    year = some_date.year
    month = some_date.month
    next_day = some_date.day + 1
    if next_day > get_days_count_by_month(month, year):
        next_day = 1
        month += 1
        year, month = get_next_year(year, month)
    return date(year, month, next_day)


def get_next_year(year, month):
    """Возвращает следующий год и 1-й месяц, если количество месяцев превысило годовое

    Args:
        year: год
        month: месяц

    Returns: кортеж из года и месяца
    """
    if month > 12:
        month = 1
        year += 1
    return year, month
