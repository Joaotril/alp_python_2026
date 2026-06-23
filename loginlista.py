nomes = []
senhas = []
nome = input("Cadastre seu nome ou digite 'S' para sair: ")
while nome.upper() != "S":
    senha = input("Cadastre sua senha: ")
    nomes.append(nome)
    senhas.append(senha)
    nome = input("Cadastre seu nome ou digite 'S' para sair: ")
print('Faça login com seu nome e senha cadastrados.')
login_nome = input("Nome: ")
login_senha = input("Senha: ")
if login_nome in nomes:
    posicao = nomes.index(login_nome)
    if login_senha == senhas[posicao]:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")