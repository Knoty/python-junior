from datetime import (
    datetime,
)


def get_days_count_by_month(month, year=datetime.now().year):
    """Возвращает количество дней по месяцу

    Args:
        month: название/номер месяца
        year: год

    Returns: количество дней
    """
    long_months = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь', 1, 3, 5, 7, 8, 10, 12]
    short_months = ['апрель', 'июнь', 'сентябрь', 'ноябрь', 4, 6, 9, 11]
    if month in long_months:
        return 31
    elif month in short_months:
        return 30
    elif month == 'февраль' or month == 2:
        return feb_number_days(year)
    else:
        return 0


def feb_number_days(year):
    """Возвращает количество дней в феврале с учетом високосного года

    Args:
        year: год

    Returns: количество дней
    """
    is_leap = year % 4 == 0
    if is_leap:
        return 29
    else:
        return 28
