number = int(input('Please enter a five-digit number: '))

if number//10000 > 9:
    print('Wrong! It is not five-digit number!')
elif number//10000 < 1:
    print('Wrong! It is not five-digit number!')

else: 
    a = number//10000
    c = number//100 % 10
    e = number % 10
    b = d = 0
    x = a,b,c,d,e
    x.replace(' ', '')
    print(a,b,c,d,e)