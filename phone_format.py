phone = input('Enter your phone number: ')
template_1 = '380{}'
new = ''

for i in phone:
    if i != '(' and i !=')' and i != '-' and i != ' ':
        new += i
print(template_1.format(new[-9:]))
if len(template_1.format(new[-9:])) < 12 :
    print('Please, enter your phone number again:')