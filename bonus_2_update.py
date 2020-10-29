A = input('Enter first number: ')
B = input('Enter second number: ')
C = input('Enter third number: ')

try:
    A, B, C = int(A), int(B), int(C)
except:
    print(A,B,C)
else:
    print(max(A, B, C))
    print(min(A, B, C))