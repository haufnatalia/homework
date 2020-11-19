"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).
    Перед записью в файл привести номер к формату +380501234567.
"""
import codecs
from os import linesep
import string



with codecs.open('phone_book.txt', 'r', encoding='utf-8') as phone:
    letter_m = 'М'
    letter_a = 'а'
    lst = phone.read().split()
    for i in lst:
        if i.startswith(letter_m) or i.endswith(letter_a):
            print(i)
            with open('edited_phone_book.txt','w', encoding='utf-8') as new:
                print(new.write(i))
        # for i in lst:
        #     if i.startswith(letter_m) or i.endswith(letter_a):
        #         print(i)


