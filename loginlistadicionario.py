nomes = {}
nome = input("Cadastre seu nome ou digite 'S' para sair: ")
while nome.upper() != "S":
    senha = input("Cadastre sua senha: ")
    nomes[nome] = senha

    nome = input("Cadastre seu nome ou digite 'S' para sair: ")
print('Faça login com seu nome e senha cadastrados.')
login_nome = input("Nome: ")
login_senha = input("Senha: ")
if nomes[login_nome] == login_senha:
        print("Login bem-sucedido!")
else:
        print("Login incorreto.")
 