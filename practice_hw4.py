string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

print('1.',string.replace(',', ' ')) 

print('2.', string.rfind('s'))

print('3.', string.count('i') + string.count('I'))

a = string.find('simply')
b = string.find('of')
print('4.', (string[a:b]).replace(',', '')) 

c = len(string)//2

print('5.', (string[:c]*3) + string[c:])