choice = 'y'

while choice == 'y':

    n = int(input('Enter the number of variables: '))
    operator = input('Enter +, -, *, /: ')
    a = int(input('Enter the number: '))

    for i in range(n-1):
        number = int(input('Enter the number: '))
        if operator == '+':
            a += number
        elif operator =='-':
            a -= number
        elif operator =='*':
            a *= number
        elif operator =='/':
            a /= number
    print('Result = ',a,'Continue? y/n')

    choice = input()
    if choice == 'n':
        print('Bye')
        break
