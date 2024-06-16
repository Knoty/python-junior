"""
Вывод:
3
3
т.к. внутри printer() значение number переопределяется на 3, а сама number объявляется как nonlocal,
что позволяет переопределить значение переменной number по-последнему присвоению в ближайшей enclosing области,
за исключением global области.
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)