from math import sqrt

x1 = int(input('Digite x1:'))
x2 = int(input('Digite x2:'))
y1 = int(input('Digite y1:'))
y2 = int(input('Digite y2:'))

P1 = x2-x1
P2 = y2-y1
d= sqrt((P1**2)+ (P2**2))
print(f'A distância é {d:.2f}')