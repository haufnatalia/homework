a = input('Enter first number: ')
operator = input('Operator (+,-,*,/)')
b = input('Enter second number: ')

try: a, b = int(a), int(b)
except ValueError:
    print('Symbols are incorrect')
else:
    if operator =='+':
        print(a + b)

    elif operator =='-':
        print(a - b)

    elif operator =='*':
        print(a * b)

    if b is 0:
        print ('zero')

    if b is not 0:
        if operator =='/':
            print(a / b)