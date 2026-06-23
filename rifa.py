import random
nomes = []
print('Digite os nomes que deseja adicionar na lista. Digite S para sair.')
nome = input("Nome: ")
while nome.upper() != "S":
    nomes.append(nome)
    nome = input("Nome: ")
sorteado=random.choice(nomes)
print(f'O nome sorteado foi: {sorteado}, parabéns!')