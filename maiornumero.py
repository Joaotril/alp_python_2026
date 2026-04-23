n1 = int(input('digite o número 1'))
n2 = int(input('digite o número 2'))
n3 = int(input('digite o número 3'))
if n1 == n2 or n1==n3 or n2 == n3:
    exit()
if n1 > n2 and n1 > n3:
    print(f'o maior número é {n1}, o primeiro número')
if n1 < n2 and n2 > n3:
    print(f'o maior número é {n2}, o segundo número')
if n1 < n3 and n3 > n2:
    print(f'o maior número é {n3}, o terceiro número')