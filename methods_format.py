s = input('Enter some string: ')

count_l = 0
count_u = 0

template_1 = 'Original: {}'
template_2 = 'Result: {}'
for i in s:
    if i.islower():
        count_l += 1
    elif i.isupper():
        count_u += 1

print('1.',template_1.format(s))

if count_l > count_u:
    print(template_2.format(s.lower()))
elif count_l < count_u:
    print(template_2.format(s.upper()))
elif count_l == count_u:
    print(template_2.format(s.swapcase()))

print('2.',template_1.format(s))

if s.istitle():
    print(template_2.format('done. '+ s))
else:
    print(template_2.format('draft: '+ s[5:]))

print('3.',template_1.format(s))

if len(s) > 20:
    print(template_2.format(s[:20]))
else:
    print(template_2.format(s + "@" * (20 - len(s))))