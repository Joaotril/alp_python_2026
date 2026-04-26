valor = float(input('Digite o valor da compra'))
print('''1.À vista
2.Cartão de débito
3.Cartão de crédito''')
pg = int(input('Forma de pagamento'))
if pg == '1':
    print(f'O valor total da compra é {valor-(valor*15/100)}')
elif pg == '2':
    print(f'O valor total da compra é {valor-(valor*10/100)}')
elif pg=='3':
        print(f'O valor total da compra é {valor-(valor*5/100)}')
else:
    print('Forma de pagamento inválida')