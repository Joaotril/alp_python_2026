print('''Calculadora simples
1.Soma
2.Subtração
3.Multiplicação
4.Divisão''')
opcao = float(input('Selecione a operação: '))
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if opcao == 1:
    print(f'O resultado da soma é {n1+n2}')
elif opcao == 2:
    print(f'O resultado da subtração é {n1-n2}')
elif opcao == 3:
    print(f'O resultado da multiplicação é {n1*n2}')
elif opcao == 4:
    print(f'O resultado da divisão é {n1/n2}')