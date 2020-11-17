"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно (не влияет на оценку):
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""
a = input('Hi, choose password complexity - 1.easy, 2.medium, 3.hard, 4.enter the length 5.your variant: ')

from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits,  punctuation

def main():
    tmp = ascii_lowercase
    tmp_2 = tmp + ascii_uppercase + digits
    tmp_3 = tmp_2 + punctuation
    if a == '1':
        password_1 = ''.join(choice(tmp) for i in range (8))
        print(password_1)
    if a == '2':
        password_2 = ''.join(choice(tmp_2) for i in range (8))
        print(password_2)
    if a == '3':
        password_3 = ''.join(choice(tmp_3) for i in range(randint(8, 16)))
        print(password_3)
    if a == '4':
        password_4 = ''.join(choice(tmp_3) for i in range(int(input('Choose password length (less than 8 is unreliable): '))))
        print(password_4)
    if a == '5':
        b = input('Enter your symbols for password: ')
        password_5 = ''.join(choice(b.replace(' ', '')) for i in range(int(input('Choose password length (less than 8 is unreliable): '))))
        print(password_5)
main()

