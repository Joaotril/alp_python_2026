print('''Calculadora simples
1.Soma
2.Subtração
3.Multiplicação
4.Divisão
0.Sair''')
opcao = float(input('Selecione a operação: '))
while opcao <0 or opcao > 4:
    print('Opção inválida')
    opcao = float(input('Selecione a operação: '))
if opcao == 0:
    print('Saindo...')
    exit()
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if opcao == 1:
    print(f'O resultado da soma é {n1+n2}')
elif opcao == 2:
    print(f'O resultado da subtração é {n1-n2}')
elif opcao == 3:
    print(f'O resultado da multiplicação é {n1*n2}')
elif opcao == 4:
    if n2 == 0:
        print('Essa divisão é impossivel')
    else:
        print(f'O resultado da divisão é {n1/n2}')