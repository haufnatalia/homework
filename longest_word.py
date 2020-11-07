s = input('Enter some string: ')
l = len(s)
count_w = 0
stop = 0
count_l = 0
lw = 0
ind = 0

for i in (s):
    if i.isalpha() and i != ' ' and stop == 0:
        count_w += 1
        stop = 1
    elif i == ' ':
        stop = 0

for i in range (l):
    if s[i].isalpha() and i != ' ':
        count_l += 1
    else:
        if count_l > lw:
            lw = count_l
            ind = i - count_l
        count_l = 0
    if count_l > lw:
        lw = count_l
        ind = i - count_l + 1

print(count_w)
print(s[ind:ind+lw],len(s[ind:ind+lw]))