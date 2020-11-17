"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

        Программа выводит сообщение:

        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********

"""

from string import ascii_lowercase, ascii_uppercase, digits

def main():
    phone = input_phone()
    email = input_email()
    password = input_password()
    print('Congratulations on successful registration')
    print('Your number: ', phone) 
    print('Your email: ', email) 
    print('Your password: ', password)
    

def input_phone(): 
    p = input('Enter your phone number: ')
    template_1 = '380{}'
    new = ''

    for i in p:
        if i != '(' and i !=')' and i != '-' and i != ' ':
            new += i
    phone = template_1.format(new[-9:])
    if len(template_1.format(new[-9:])) < 12:
        print('Wrong number')
        return input_phone()
        

def input_email():
    e = input('Enter your email: ')
    if len(e) >= 6 and e.count('@') == 1:
       email = e
    else:
        print('Wrong email')
        return input_email()

minimum_characters = 8
error = 0

def input_password(): 
    pw = input('Enter your password: ')
    pwlength = len(pw)
    minimum_characters = 8
    error = 0
    if pwlength < minimum_characters:
        error += 1
        print ('Not a valid password. Must contain AT LEAST 8 characters.')
        return input_password()
    if pw.isalpha():
       error += 1
       print('The password must contain at least 1 digits.')
       return input_password()
    if pw.isdigit():
       error += 1
       print('The password must contain at least 2 letters.')
       return input_password()
    if pw.isupper():
       error += 1
       print('You need at least one lower case letter.')
       return input_password()
    if pw.islower():
       error += 1
       print('You need at least one upper case letter.')
       return input_password()   
    if " " in pw:
       error += 1
       print('Please, do not use spase.')
       return input_password()  
    pwrepit =input('Repit password: ')
    if pwrepit != pw:
        print('Wrong password')
        return input_password()
    password = pw


 

main()

