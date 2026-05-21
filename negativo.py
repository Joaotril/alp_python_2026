soma = 0
media = 0
num = int(input("Digite um número: "))
maior = num

while num >= 0:
    soma = soma + num
    media = media + 1
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
if num < 0:
    print(f'A soma dos números é {soma}')
    print(f'A média dos números é {soma / media}')    
    print(f'O maior número é {maior}')
