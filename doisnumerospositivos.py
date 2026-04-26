n1 = int(input('Primeiro número'))
n2 = int(input('Segundo número'))

print('''1. Média ponderada, pesos 2 e 3
2. Quadrado da soma dos 2 números
3. Cubo do menor número''')
opcao=input('Escolha uma opção:')

if opcao == '1':
    print(f'A média ponderada é {(n1*2+n2*3)/(2+3)}')
    
elif opcao == '2':
    print(f'O quadrado da soma é {(n1+n2)**2}')
    
elif opcao=='3':
    if n1<n2:
        print(f'O cubo do menor número é {n1**3}')
    elif n1>n2:
        print(f'O cubo do menor número é {n2**3}')
    elif n1==n2:
        print('Os números são iguais')
else:
    print('Opção inválida') 
    exit()
    