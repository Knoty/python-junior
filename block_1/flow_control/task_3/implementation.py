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
    long_months = {'январь': 1, 'март': 3, 'май': 5, 'июль': 7, 'август': 8, 'октябрь': 10, 'декабрь': 12}
    short_months = {'апрель': 4, 'июнь': 6, 'сентябрь': 9, 'ноябрь': 11}
    if month in long_months or month in long_months.values():
        return 31
    elif month in short_months or month in short_months.values():
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
