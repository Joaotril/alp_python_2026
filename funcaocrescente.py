def recebe (lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista [j +1] = lista [j +1], lista [j]
    return lista
lista=[]
quantidade = int(input('DIgite quantos número você quer colocar na lista: '))
for i in range(quantidade):
    num = int(input(f'Digite o {i+1}º número '))
    lista.append(num)
print('Sua lista ordenada é: ', recebe(lista))