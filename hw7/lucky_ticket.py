"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    a = sum(map(int,str(ticket_num)[:len(str(ticket_num))//2]))
    b = sum(map(int,str(ticket_num)[len(str(ticket_num))//2:]))
    a == b is True
    return a == b
    
assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

