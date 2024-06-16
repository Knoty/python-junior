"""
Вывод:
Test message
None
т.к. "Test message" передано аргументом в transmit_to_space и его print, определенный в data_transmitter,
вызывается на 16й строке.
"None" т.к. transmit_to_space, указанный в качестве аргумента print на 19й строке не имеет возвращаемого значения.
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
