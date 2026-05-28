soma = 0
for i in range(1, 6):
    med = input(f'Nome do {i}º medicamento:')
    preco = float(input(f'Preço {i}º do medicamento:'))
    if i == 1:
        mbarato = med
        pbarato = preco
    elif preco < pbarato:
        mbarato = med
        pbarato = preco
    soma += preco

print(f'O medicamento mais barato é {mbarato} com o preço de {pbarato}')
print(f'A média dos preços é {soma/5}')